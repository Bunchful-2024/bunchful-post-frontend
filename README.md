# Bunchful Post
- Author: Stephanie Chen  
- Date: 07/03/2024 last update
- Reference: [Writing Design Doc](https://medium.com/machine-words/writing-technical-design-docs-71f446e42f2e), [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/#apis)

# Introduction 
## Rationale  
As Bunchful expands its content platform presence, managing posts becomes challenging due to the manual, repetitive process required for each platform. Tailoring content to each platform's unique style is also time-consuming, reducing productivity and limiting audience engagement. While there are existing social media management tools, they couldn't fulfill the needs of Bunchful as most of them focus on popular platforms like Facebook, Instagram, etc. Thus, the team is building a tool for Bunchful to manage its content over 19 platforms.  
## Non-goals
1. This project doesn't include the following functions: Post Scheduling, Performance Analytics.
2. This project at the current stage aims to integrate 4-5 social media platforms, gradually increasing the amount.

# Proposed Design  
## Overview
Bunchful Post is an AI-powered web application that assists in content management.  
It has two main functions: Content Curation and Automated Posting.  
- Content Curation: Leverages ChatGPT to compose tailored content for various platforms. It assists in crafting customized content style for each platform, such as social media posts, articles, blogs, and newsletters.  
- Automated Posting: Users can seamlessly upload posts to platforms like Facebook and LinkedIn with a single click. It eliminates the need for manual uploading, saving time and effort. 
## System Architecture
### 1. Client Layer:
  - Web Interface
### 2. Application Layer:
  - AI Integration (ChatGPT)
  - Automation Engine
  - API Gateway
### 3. Integration Layer:
  - Third-Party API Integrations (Social Media, Analytics)
  - Authentication Services
### 4. Infrastructure Layer:
  - Hosting (Cloud Services)

## Implementation
### 1. Backend Development: 
- Set up the backend using Flask. 
- Integrate OpenAI’s API for content generation. 
- Integrate social media third-party APIs. 
 
### 2. Frontend Development: 
- Design UI in Figma. 
- Develop the frontend using Streamlit. 
 
### 3. Deployment:
- Deploy the web app on Render cloud services. 

# Impact
Bunchful Post not only increases work efficiency, but also plays an important role in creating potential revenue for Bunchful. 
 
- Increase work efficiency: Automating posting tasks saves time and effort, improving productivity. 
Engage with diverse audiences: Tailored content enables us to engage with different audiences better. It helps foster stronger connections across various social media channels. 
- Create potential revenue: Improved content management and audience engagement increase visibility, leading to more monetization opportunities.

# Alternatives
