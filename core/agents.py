import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from core.state import ContentState

# 1. Load the environment variables FIRST
load_dotenv()

# 2. Check if the key is actually loaded (helps with debugging)
if not os.getenv("OPENAI_API_KEY"):
    print("CRITICAL WARNING: OPENAI_API_KEY is missing from your environment variables!")

# 3. Now it is safe to initialize the LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

def analyze_voice(state: ContentState):
    prompt = ChatPromptTemplate.from_template(
        "Analyze this text and extract the core brand voice, tone, and pacing in 2 sentences. "
        "Text: {text}"
    )
    chain = prompt | llm
    res = chain.invoke({"text": state["source_text"]})
    return {"brand_voice": res.content}

def reel_agent(state: ContentState):
    prompt = ChatPromptTemplate.from_template(
        "Write a 20-30 second Instagram Reel script based on the text below. "
        "Brand Voice: {voice}\nText: {text}\n\n"
        "Rules: High-retention hook. 2 columns: [Visual] | [Audio]. No generic fluff."
    )
    chain = prompt | llm
    res = chain.invoke({"voice": state["brand_voice"], "text": state["source_text"]})
    return {"reel_script": res.content}

def carousel_agent(state: ContentState):
    prompt = ChatPromptTemplate.from_template(
        "Create EXACTLY a 6-slide carousel from this text.\n"
        "Brand Voice: {voice}\nText: {text}\n\n"
        "Rules: For EACH slide provide: 1. Headline, 2. Copy, 3. Visual Direction. "
        "Slide 1 is a hook. Slide 6 is a CTA."
    )
    chain = prompt | llm
    res = chain.invoke({"voice": state["brand_voice"], "text": state["source_text"]})
    return {"carousel": res.content}

def twitter_agent(state: ContentState):
    prompt = ChatPromptTemplate.from_template(
        "Write a Twitter/X thread (minimum 5 tweets) based on this text.\n"
        "Brand Voice: {voice}\nText: {text}\n\n"
        "Rules: Tweet 1 is a scroll-stopping hook. Punchy sentences. No cringe hashtags."
    )
    chain = prompt | llm
    res = chain.invoke({"voice": state["brand_voice"], "text": state["source_text"]})
    return {"twitter_thread": res.content}

def static_agent(state: ContentState):
    prompt = ChatPromptTemplate.from_template(
        "Write a static LinkedIn/Instagram caption from this text.\n"
        "Brand Voice: {voice}\nText: {text}\n\n"
        "Rules: Strong hook, good use of whitespace, end with a question to drive comments."
    )
    chain = prompt | llm
    res = chain.invoke({"voice": state["brand_voice"], "text": state["source_text"]})
    return {"static_caption": res.content}