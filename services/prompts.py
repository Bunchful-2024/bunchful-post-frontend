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
Correlate 3 images to the {topic} and {keyword} with article content, marking the images like this format [Image index: image descrtiption],
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
Generate a catchy, passive-voice footer inviting engagement, encouraging readers to share their thoughts and join the conversation using {hashtags}, and inform them about additional resources. 
Avoid using words like "captivate," "tapestry," "delve," "foster," "endeavor," "embark," and "unleash."
Use contractions, colloquialisms, and approachable language to make the post relatable and human, subtly mentioning our company, {company_name}, to reinforce our brand's presence and reliability without sounding biased. Give placholder for affliate link as well.
Do not include a headline and any text formatting for the post, only include plain text. 
Show the below attributes with the separation line.
Suggest one image description based on the {topic} and {keyword} for retrieval, mark it like this [Image].
The description should be 10 words or less, do not use symbols.
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
The content should be engaging, written in a human-like style, and formatted for easy readability. Emphasize {keyword} and its impact, using a narrative in passive voice with catchy phrases that keep the reader scrolling. 
Personalize the newsletter with elements like the recipient's name or a tailored greeting. Include a clickbait-style call to action for affiliate links, making it irresistible for the audience to click. 
Suggest correlating images for {topic} and {keyword}, labeled as [Image 1], with descriptions of 10 words or less. 
Use {hashtags} strategically to boost social media engagement. Ensure the content stays within the {character_limit}, with perfect grammar and smooth transitions, creating a natural flow that doesn't feel entirely AI-generated. 
Incorporate a mix of content types such as short articles, bullet points, quotes, to add variety and maintain interest. 
Optimize the newsletter for mobile devices, ensuring a responsive design that looks good on smaller screens. 
Include an attention-grabbing preview text that complements the subject line to entice readers to open the email. 
Add interactive elements like polls, quizzes, or embedded videos to engage the audience actively. 
Incorporate social proof, such as testimonials, case studies, or user-generated content, to build trust and credibility.
Maintain a good balance between text and visuals to avoid overwhelming the reader, and use whitespace effectively to enhance readability.  
Conclude with a well-crafted footer that reinforces the newsletter's purpose and includes any necessary legal disclaimers or contact information.

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

def listicles(platform, character_limit, topic, keyword,hashtags):
    return f"""
Create an SEO-focused listicle for {platform} that not only grabs attention but outshines the competition.
Start by selecting highly relevant and targeted keywords for the {topic} that are ideal for listicle content, ensuring they resonate with your audience and boost search engine ranking. 
Craft a compelling headline that includes the number of items, giving readers a clear idea of what to expect.
Begin with a brief, engaging introduction that sets the context and naturally incorporates the keyword {keyword} to enhance visibility. 
Organize the list with relevant and logically ordered items, using subheadings to make it easy to navigate. 
For each item, provide in-depth content with actionable steps or detailed insights that offer real value to the reader. 
Make sure the keyword {keyword} is smoothly integrated throughout the content to improve search rankings. 
Go the extra mile by making your listicle more comprehensive and longer than competing articles. 
Include all the extra details that make the content not only informative but also engaging and authoritative. 
Design the listicle with a pro-level layout, ensuring its visually appealing and easy to read. 
Add top-quality infographics and visuals like images or videos where appropriate, labeled as [Image 1], [Image 2], etc., with descriptions of 10 words or less to enhance engagement and make complex information easier to digest.
Conclude with a summary or a strong call to action that reinforces the main points and encourages reader interaction. 
Use relevant {hashtags} strategically to boost social media engagement and reach a wider audience. 
Ensure the content stays within the {character_limit}, with perfect grammar, smooth transitions, and a professional finish that doesn't feel entirely AI-generated.

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