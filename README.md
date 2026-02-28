⚙️ The Tiny Content Machine
Overview
The Tiny Content Machine is an AI-powered, multi-agent orchestration system that atomizes a single piece of long-form text (like a podcast transcript, blog post, or interview) into multiple platform-native social media assets.

Instead of generating generic, templated content, the system first analyzes the input to extract the unique Brand Voice, ensuring all output feels authentic to the original author.

System Architecture
The core of the application is built using LangGraph to manage state and parallel agent execution.

Input Phase: The user provides long-form text via the Streamlit UI.

Analyzer Node (Sequential): The system passes the text to a Brand Voice Agent to extract tone, pacing, and vocabulary.

Generation Nodes (Parallel): Once the voice is established, the system triggers four distinct agents simultaneously to drastically reduce generation time:

Reel Agent: Writes a 20-30s video script with visual/audio columns.

Carousel Agent: Formats a strict 6-slide LinkedIn/Instagram carousel.

Twitter Agent: Drafts a punchy, 5+ tweet thread.

Static Agent: Writes a high-engagement, whitespace-optimized post.

Output Phase: The populated state is returned to the Streamlit UI and organized into clean, accessible tabs.

Tech Stack
Orchestration: LangGraph, LangChain

LLM: OpenAI GPT-4o (langchain-openai)

Frontend/UI: Streamlit

Language: Python 3.11+

test the application:
Live link:https://tiny-content-machine.streamlit.app
