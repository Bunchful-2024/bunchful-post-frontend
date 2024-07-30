# helper functions

# function to extract the generated content from the output string
def extract_generated_content(output_string):
    # Define the delimiters for the Generated Content section
    content_start = "**Generated Content:**"
    content_end = "**Images:**"

    # Find the start and end positions of the content
    start_index = output_string.find(content_start)
    end_index = output_string.find(content_end)

    if start_index == -1 or end_index == -1:
        # Delimiters not found, return None or an empty string
        return None

    # Extract the content between the delimiters
    start_index += len(content_start)  # Move index to the start of the actual content
    generated_content = output_string[start_index:end_index].strip()

    return generated_content
