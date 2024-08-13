#predefined prompts for Gemini to use from

#prompt on line 20 are required for text extraction
def general_prompt(platform, character_limit, topic, keyword,company_name,hashtags):
    return f"""
Create a {platform} article that highlights the significance of {topic} using a clickbait-style title and focusing on {keyword}. The article should adhere to AP format, with simple font styles headings in H2, and body text in normal font. Write in an engaging, conversational style using idioms and varied sentence structures, incorporating over 30% transition words for readability. Add a block quote related to the {topic} if necessary.
Start with a compelling introduction related to {topic} and use clear headings or bullet points if needed and ensure the article length adheres to the recommended character count for optimal engagement: {platform}: {character_limit}. 
Add a clear CTA to encourage interaction, such as asking readers to comment, share, or follow a link. 
Pose a question at the end to prompt discussion, and strategically use hashtags such as {hashtags} to increase the article’s reach and engagement. Mention and tag relevant organizations or individuals to increase visibility and interaction. Proofread the content to ensure it is free of grammatical errors and readability. Enhance the article with emojis and remove any placeholders. 
Formatting:
    - Headings: H2
    - Body Text: Normal font
    - Paragraphs: Vary length for impact
Add placeholders for up to three affiliate links to be included.
Please generate text that avoids using formal or overly academic phrases such as 'it is worth noting,' 'furthermore,' 'consequently,' 'in terms of,' 'one may argue,' 'it is imperative,' 'this suggests that,' 'thus,' 'it is evident that,' 'notwithstanding,' 'pertaining to,' 'therein lies,' 'utilize,' 'be advised,' 'hence,' 'indicate,' 'facilitate,' 'subsequently,' 'moreover,' and 'it can be seen that.' 

Aim for a natural, conversational style that sounds like two friends talking at the coffee shop. Use direct, simple language and choose phrases that are commonly used in everyday speech. 
If a formal phrase is necessary for clarity or accuracy, you may include it, but otherwise, please prioritize making the text engaging, clear, and relatable. 

Generate a catchy footer in passive voice that encourages engagement and conversation. Include a call to action for readers to share their thoughts in the comments and spread the word. Mention using the {hashtags} to join the conversation and inform readers for more resources. 
Avoid these words: Captivate, Tapestry, Delve, Foster, Endeavor, Embark, Unleash.

Use contractions, colloquialisms, and approachable language throughout the article.
When writing the article, please use our company name, {company_name}, at a few different points. It should be clear to the reader that we are the ones writing this post.
Do NOT be pushy or salesy with your writing style. We want the reader to know our company exists and that it solves the problem the article is discussing, but the style should not come across as biased. This is VERY important. 
The reader should sense we are very human just like them, we understand their problems, and we seek to honestly give them accurate information, in a fun, casual way.”
Clarify the concepts in the article by anchoring them in vivid, conceivable real-life scenarios. Feel free to craft illustrative anecdotes that shed light on the subject matter. 
Transparency is key here—ensure that these hypothetical situations are presented as fictional examples, NOT as factual occurrences, as we want to maintain integrity with the reader.
The introduction of the article should identify the problem the buyer has and contextualize who they are. 
It should also outline what the reader will get and learn from reading the post, and the payoff that will come with completing the content.
Vary the length of the paragraphs and sentences in these writings. Look for opportunities to create punchy, incisive moments to land your points, while at other times produce paragraphs that are 2-4 sentences as needed.
Correlate 3 images to the {topic} and {keyword}, marking the images like this [Image 1], [Image 2], [Image 3]
The image description should be 10 words or less, do not use symbols.

Show the below attributes with the separation line.
Show 7 optimal posting days and times with EST time zone based on the highest engagement activity.
Add a title **Optimal Posting Days and Times (EST):** for this section.
Make the Content 95 percent or greator human genereated.
Show the below attributes with the separation line.
Article Attributes. Bullet these:
    Word Count
    Character Count
    Cost for Article for API
    Keywords
    SEO Seobility Score
    Readability Score
    Estimated Reading Time
    Engagement
    Call to Action
    number of backlinks
    Brand mention
    sentiment
    Citation links:
    """

# platform_character_limits = {
#     'LinkedIn': 2000,
#     'Facebook': 1500,
#     'Instagram': 1300,
#     'X (Twitter)': 280,
#     'Instagram Threads': 500
# }

# def generate_post(topic, platform):
#     character_limit = platform_character_limits.get(platform, 500)  # Default to 500 if platform not found
#     prompt = general_prompt(platform, character_limit)
#     # Add code to generate the post using the prompt
#     return prompt.format(Topic=topic)


# #example usage
# topic = "The importance of sustainable business practices"

# linkedin_post = generate_linkedin_post(topic)
# facebook_post = generate_facebook_post(topic)
# instagram_post = generate_instagram_post(topic)
# twitter_post = generate_twitter_post(topic)
# threads_post = generate_threads_post(topic)

# # Print or use the generated posts
# print("LinkedIn Post:\n", linkedin_post)
# print("Facebook Post:\n", facebook_post)
# print("Instagram Post:\n", instagram_post)
# print("Twitter Post:\n", twitter_post)
# print("Threads Post:\n", threads_post)


# # migrate the cost estimation logic to the main file
# # Show the Estimated Cost per article below with a sepeartion line considering the input and output tokens.
# # Writer AI Cost projection per article
# # Total Output Token Count=  prompt_char_count + generated_char_count
# # Input per token price: 7.50/1,000,000 = 0.0000075 per token
# # Output per token price: 22.50/1,000,000=0.0000225 per token
# # Cost of article: (Total Output Token Count * $30.00) / 1,000,000