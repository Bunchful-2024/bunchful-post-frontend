# Bunchful Post
🙌 [Bunchful Post on Streamlit Cloud](https://bunchful-post.streamlit.app)<br>
- Project documentatoin by Stephanie and Deep
- Date: 09/02/2024 last update

# 0. Overview 

Bunchful Post is an AI-powered web application that assists in content management over several platforms. The app not only increases work efficiency for Bunchful Team but also serves as an important tool in creating potential revenue for Bunchful.

# 1. Rationale 
As Bunchful expands its content platform presence, managing posts becomes challenging due to the manual, repetitive process required for each platform. Tailoring content to each platform's unique style is also time-consuming, reducing productivity and limiting audience engagement. 

While there are existing tools, they couldn't fulfill Bunchful's need to focus on article platforms such as Medium, Hub Pages, etc. 

# 2. Functions
## 2.1 Functions Overview
Bunchful Post is an AI-powered web application that assists in content management. It has two main functions: Content Generation and Automated Posting.  
- Content Curation: Leverages Gemini to compose tailored content for various content types. Considering diverse target audiences, it assists in crafting customized content, such as social media posts, articles, blogs, and newsletters.  
- Automated Posting: After generating content, users can directly publish the content to the platforms with a single click. It eliminates the need for manual uploading, saving time and effort. 

## 2.2 Non-goals
- This project doesn't support the following functions: Posting to Multiple Platforms at once, Post Scheduling, and Performance Analytics.

- This project currently supports posting on Medium and Facebook, gradually increasing the amount of platforms.

# 3. Tech Stack
Bunchful Post is developed and deployed in Streamlit. We selected Streamlit for the framework as it works well with LLMs. It's also easy to pick up and suitable for fast iteration. Furthermore, Streamlit Cloud offers a free deployment plan.
- Website: Python Streamlit
- Third-party APIs
  - Platform: Medium, Facebook
  - Image Retrievals: Pexels
  - LLMs: Gemini
- Tools:
  - Deployment: Streamlit Cloud 
  - Version control: Git/GitHub
  - Project Management: Jira

# 4. Impact
Bunchful Post not only increases work efficiency, but also plays an important role in creating potential revenue for Bunchful. 
 
- Increase work efficiency: Automating posting tasks saves time and effort, improving productivity. 
- Engage with diverse audiences: Tailored content enables the team to engage with different audiences better. It helps foster stronger connections across various social media channels. 
- Create potential revenue: Improved content management and audience engagement increase visibility, leading to more monetization opportunities such as affiliate marketing.
