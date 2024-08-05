# helper functions
import streamlit as st
import re

# function to extract the generated content from the output string
def extract_generated_content(content):
    """
    Extract the generated content from the given content before the "Images" section.

    Args:
        content (str): The complete content including the "Images" section.

    Returns:
        str: The extracted generated content before the "Images" section.
    """
    # Split the content by the "Images:" keyword
    split_content = content.split("**Images:**", 1)
    
    # Return the content before the "Images" section if it exists
    if len(split_content) > 1:
        return split_content[0].strip()
    else:
        # Return the full content if "Images:" section is not found
        return content.strip()
    
def transform_to_markdown(input_string):
    # Replace "##" with "#"
    transformed_string = input_string.replace("##", "#")
    # Specify the new line character
    transformed_string = transformed_string.replace("\n", "\n\n ")
    # Define the image to markdown conversion function
    def image_to_markdown(match):
        full_caption = match.group(0)  # The entire match, including "Image X: Caption"
        caption = match.group(1)       # The actual caption text
        # Fetch the corresponding image link from the dictionary
        image_link = st.session_state.image_mapping.get(full_caption, "Image Link")  # Default to "Image Link" if full_caption not found
        return f"![{caption}]({image_link})"
    
    # Replace "[Image X: Caption]" with "![Caption](Image Link)"
    transformed_string = re.sub(r"\[Image \d+: (.+?)\]", image_to_markdown, transformed_string)
    
    return transformed_string

def update_formatted_text():
    st.session_state.formatted_text = transform_to_markdown(st.session_state.edited_text)

def extract_title(markdown_string):
    # Split the input string by the specified new line character
    lines = markdown_string.split("\\n")
    # Iterate through the lines to find the first heading
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line.startswith("#"):
            # Remove the leading "#" and return the rest as the title
            return line.lstrip("#").strip()
    # If no title found, return None
    return None

#function to extract the sentences for Pexels retrieval
def extract_image_captions(text):
    lines = text.split('\n')
    image_captions = []

    for line in lines:
        line = line.strip()
        if line.startswith("[Image"):
            # Extract the caption text within the square brackets
            start = line.find('[') + 1
            end = line.find(']')
            if start != -1 and end != -1:
                caption = line[start:end]
                image_captions.append(caption)
    
    return image_captions

def reset_session_state():
    for key in st.session_state.keys():
        del st.session_state[key]