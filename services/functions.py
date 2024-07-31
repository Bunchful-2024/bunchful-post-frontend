# helper functions
import streamlit as st

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
    return transformed_string

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


def reset_session_state():
    for key in st.session_state.keys():
        del st.session_state[key]