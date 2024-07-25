#predefined prompts for Gemini to use from

def general_prompt():
    return """
Create a {platform} post highlighting the significance of {Topic}. Use primary keywords in italics, with a keyword density of less than 2% (i.e., less than twice per 100 words). Write in an engaging, conversational style using idioms and varied sentence structures, incorporating over 30% transition words for readability. Start with a compelling introduction related to {Topic} and use clear headings or bullet points if needed. Include a link to a relevant resource or further reading and ensure the post length adheres to the recommended character count for optimal engagement:
LinkedIn: {LinkedIn_Character_Limit}
Facebook: {Facebook_Character_Limit}
Instagram: {Instagram_Character_Limit}
X (Twitter): {Twitter_Character_Limit}
Instagram Threads: {Threads_Character_Limit}
Add a clear CTA to encourage interaction, such as asking readers to comment, share, or follow a link. Pose a question at the end to prompt discussion. Use relevant images or media with descriptive alt text to enhance visual appeal, and strategically use hashtags such as #BeBunchful, #BunchfulSDGs, #GivingBack, #SocialImpact, #BunchfulAtlas, #BunchfulEvents, #BunchfulNews, #NewYork, #UNSDGs, #Philanthropy to increase the post’s reach and engagement.
Mention and tag relevant organizations or individuals to increase visibility and interaction. Proofread the content to ensure it is free of grammatical errors and readability.
Please generate text that avoids using formal or overly academic phrases such as 'it is worth noting,' 'furthermore,' 'consequently,' 'in terms of,' 'one may argue,' 'it is imperative,' 'this suggests that,' 'thus,' 'it is evident that,' 'notwithstanding,' 'pertaining to,' 'therein lies,' 'utilize,' 'be advised,' 'hence,' 'indicate,' 'facilitate,' 'subsequently,' 'moreover,' and 'it can be seen that.' Aim for a natural, conversational style that sounds like two friends talking at the coffee shop. Use direct, simple language and choose phrases that are commonly used in everyday speech. If a formal phrase is necessary for clarity or accuracy, you may include it, but otherwise, please prioritize making the text engaging, clear, and relatable.
Avoid these words: embark
Use contractions, colloquialisms, and approachable language throughout the article.
When writing the article, please use our company name, which is Bunchful Enterprise, at a few different points. It should be clear to the reader that we are the ones writing this post.
Do NOT be pushy or salesy with your writing style. We want the reader to know our company exists and that it solves the problem the article is discussing, but the style should not come across as biased. This is VERY important. The reader should sense we are very human just like them, we understand their problems, and we seek to honestly give them accurate information, in a fun, casual way.”
Clarify the concepts in the article by anchoring them in vivid, conceivable real-life scenarios. Feel free to craft illustrative anecdotes that shed light on the subject matter. Transparency is key here—ensure that these hypothetical situations are presented as fictional examples, NOT as factual occurrences, as we want to maintain integrity with the reader.
The introduction of the article should identify the problem the buyer has and contextualize who they are. It should also outline what the reader will get and learn from reading the post, and the payoff that will come with completing the content.
Vary the length of the paragraphs and sentences in these writings. Look for opportunities to create punchy, incisive moments to land your points, while at other times produce paragraphs that are 2-4 sentences as needed.
Show the below attributes with the separation line.
Correlate images to the content. One from Pexels, one from Leonardo, and one from DALL-E.
Show the below attributes with the separation line.
Show 7 optimal posting days and times with EST time zone based on the highest engagement activity.
Make the Content 95 percent or greator human genereated.
Show the below attributes with the separation line.
Article Attributes. Bullet these:
-        read time
-        Token input token count
-        Total Output Token Count 
            - cost of article 
-        Inbound Estimated Cost of the Post
-        readability score
-        word count
-        character count
-        number of backlinks
-        Brand mention
-        sentiment
Show the Estimated Cost per article below with a sepeartion line considering the input and output tokens.
Writer AI Cost projection per article
Total Output Token Count=  prompt_char_count + generated_char_count
Input per token price: 7.50/1,000,000 = 0.0000075 per token
Output per token price: 22.50/1,000,000=0.0000225 per token
Cost of article: (Total Output Token Count * $30.00) / 1,000,000

    """
   