#predefined prompts for Gemini to use from

#prompt on line 20 are required for text extraction
def article(platform, character_limit, topic, keyword,company_name,hashtags):
    return f"""
Create a {platform} article that highlights the significance of {topic} using a clickbait-style title and focusing on {keyword}. The article should adhere to AP format, with simple font styles headings in H2, and body text in normal font. Write in an engaging, conversational style using idioms and varied sentence structures, incorporating over 30% transition words for readability. Add a block quote related to the {topic} if necessary.
Start with a compelling introduction related to {topic} and use clear headings or bullet points if needed and ensure the article length adheres to the recommended character count for optimal engagement: {platform}: {character_limit}. 
Add a clear CTA to encourage interaction, such as asking readers to comment, share, or follow a link. 
Pose a question at the end to prompt discussion, and strategically use hashtags such as {hashtags} to increase the article’s reach and engagement. Mention and tag relevant organizations or individuals to increase visibility and interaction. Proofread the content to ensure it is free of grammatical errors and readability. Enhance the article with emojis and remove any placeholders. 
Formatting:
    - Headings: H2
    - Body Text: Normal font
    - Paragraphs: Vary length for impact
Include placeholders for affiliate links, designed as enticing call-to-action elements with a clickbait appeal.
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

def social_media_post(platform, character_limit, topic, keyword, company_name,hashtags):
    return f"""
Create a social media post for {platform} that highlights the significance of {topic} with a catchy, clickbait-style headline focusing on {keyword}. 
The post should be engaging and conversational, using idioms and varied sentence structures with over 30% transition words for better readability. 
Start with a compelling hook related to {topic} to grab attention and use clear, concise sentences, considering bullet points or short paragraphs for clarity. 
Include a block quote related to {topic} if it adds value, and ensure the post strictly adheres to the character limit for optimal engagement: {platform}: {character_limit}. 
Encourage readers to comment, share, or follow a link, and pose a question at the end to prompt discussion. Use strategic hashtags like {hashtags} to boost reach and engagement, and tag relevant organizations or individuals to increase visibility. 
Write in a casual, friendly tone as if chatting with a friend at a coffee shop, avoiding formal or overly academic language. Be transparent and honest, clearly stating fictional examples when used. 
Suggest correlating images for {topic} and {keyword}, labeled as [Image 1], [Image 2], [Image 3], with descriptions of 10 words or less. 
Generate a catchy, passive-voice footer inviting engagement, encouraging readers to share their thoughts and join the conversation using {hashtags}, and inform them about additional resources. 
Avoid using words like "captivate," "tapestry," "delve," "foster," "endeavor," "embark," and "unleash."
Use contractions, colloquialisms, and approachable language to make the post relatable and human, subtly mentioning our company, {company_name}, to reinforce our brand's presence and reliability without sounding biased. Give placholder for affliate link as well.
Show the below attributes with the separation line.
Show 7 optimal posting days and times with EST time zone based on the highest engagement activity.
Add a title **Optimal Posting Days and Times (EST):** for this section.
Make the Content 95 percent or greator human genereated.
Show the below attributes with the separation line.
Post Attributes. Bullet these:
    Word Count
    Character Count
    Cost for the post
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

#Prompt for Newsletter
def newsletter(character_limit, topic, keyword,company_name,hashtags):
    return f"""
Craft a newsletter for {company_name} that focuses on {topic} and grabs the reader's attention right from the start. 
The content should be engaging, written in a human-like style, and formatted for easy readability. 
Make sure to emphasize {keyword} and how it impacts. The narrative should be in passive voice, using catchy phrases that entice the reader to keep scrolling. 
Include a clickbait-style call to action for affiliate links, making it irresistible for the audience to click. 
Suggest correlating images for {topic} and {keyword}, labeled as [Image 1], [Image 2], with descriptions of 10 words or less.
Use {hashtags} strategically to boost social media engagement. The content must be within the {character_limit},
with perfect grammar and smooth transitions, ensuring it feels naturally written and not entirely AI-generated.
"""

def listicles(platform, character_limit, topic, keyword,hashtags):
    return f"""
Create a listicle for the {platform} with an eye-catching title that grabs attention, keeping it within {character_limit} character limit. 
Start with a short introduction that sets up the {topic} and includes the keyword {keyword} to help with SEO search rankings. 
Organize the list in a clear, logical order, using subheadings to make it easy to navigate. 
For each item, provide a straightforward explanation and include the keyword {keyword} where it fits naturally. 
Suggest correlating images for {topic} and {keyword}, labeled as [Image 1], [Image 2], with descriptions of 10 words or less.
Wrap things up with a summary or a call to action that reinforces the main points and invites readers to engage. 
Conclude with a summary or a call to action that reinforces the main points and encourages reader interaction. 
Ensure consistent formatting and check for grammar and spelling to keep the text polished.
Use relevant {hashtags} to increase visibility and attract more readers.

Show the below attributes with the separation line.
Show 7 optimal posting days and times with EST time zone based on the highest engagement activity.
Add a title **Optimal Posting Days and Times (EST):** for this section.
Make the Content 95 percent or greator human genereated.
Show the below attributes with the separation line.
Post Attributes. Bullet these:
    Word Count
    Character Count
    Keywords
    Estimated Reading Time
    Engagement
    Call to Action
    Number of backlinks
    Brand mention
    Citation links:
"""