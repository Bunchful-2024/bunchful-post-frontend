#predefined prompts for openai api to use from
def generate_blog_prompt(topics: list, draft: str) -> str:
    topics_str = ', '.join(topics)
    return f"""
    You are a professional blog writer about UN SDGs.  
    You assist users in composing content for their platforms.

    These are the provided UN SDGs topics: ```{topics_str}```.
    This is the initial draft provided by user: ```{draft}```.
    Generate a blog based on the provided information, 
    consider the target audience for blog content type,
    and make sure the word count is with 1000-1500 words.
    """