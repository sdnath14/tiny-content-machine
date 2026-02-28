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

Repository Structure
Plaintext
tiny_content_machine/
├── .env                  # Local environment variables (ignored in Git)
├── .gitignore            # Security rules
├── requirements.txt      # Python dependencies
├── core/
│   ├── __init__.py
│   ├── state.py          # Defines the TypedDict state passed between agents
│   ├── agents.py         # Defines the LLM prompts and agent logic
│   └── graph.py          # Wires the agents together into a LangGraph workflow
└── ui/
    └── app.py            # Streamlit frontend (Imports the graph directly)
Local Setup & Installation
1. Clone the repository

Bash
git clone https://github.com/YOUR-USERNAME/tiny-content-machine.git
cd tiny-content-machine
2. Create a Virtual Environment (Recommended)

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies

Bash
pip install -r requirements.txt
4. Set up your Environment Variables
Create a .env file in the root directory and add your OpenAI API key:

Plaintext
OPENAI_API_KEY=sk-your-secret-key-here
5. Run the Application

Bash
streamlit run ui/app.py
