#predefined prompts for openai api to use from

#migrate the predefined prompt into excel files

def general_prompt():
    return """
    You are a professional blog writer about UN SDGs.  
    You assist users in composing content for their platforms.
    """
   
def generate_blog_prompt(topics: list, draft: str) -> str:
    topics_str = ', '.join(topics)
    return f"""
    These are the provided UN SDGs topics: ```{topics_str}```.
    This is the initial draft: ```{draft}```.
    Generate a blog based on the provided information, 
    consider the target audience for blog content type,
    and make sure the word count is with 1000-1500 words.
    """