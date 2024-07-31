# helper functions

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
    transformed_string = transformed_string.replace("\n", "\\n")
    return transformed_string
