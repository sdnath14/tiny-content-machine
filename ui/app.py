import streamlit as st
import os
import sys

# 1. Force Python to add the root folder to its path so it can find 'core'
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# 2. Now it is safe to import your LangGraph machine!
from core.graph import content_machine

st.set_page_config(page_title="Tiny Content Machine", layout="wide")
st.title("⚙️ The Tiny Content Machine")
st.markdown("Turn one piece of long-form content into platform-native assets.")

source_text = st.text_area("Paste your blog, article, or transcript here:", height=200)

if st.button("Generate Content Engine", type="primary"):
    if not source_text.strip():
        st.warning("Please enter some text first.")
    else:
        # Check if the API key is available (Streamlit Cloud will inject this later)
        if not os.getenv("OPENAI_API_KEY"):
            st.error("OpenAI API Key is missing! Please configure it in your environment secrets.")
        else:
            with st.spinner("Agents are analyzing voice and generating platforms in parallel..."):
                try:
                    # Run the multi-agent system directly!
                    data = content_machine.invoke({"source_text": source_text})
                    
                    st.success("Content generation complete!")
                    
                    with st.expander("Detected Brand Voice & Tone (Click to expand)"):
                        st.write(data.get("brand_voice", ""))
                    
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "📱 Instagram Reel", 
                        "🎠 6-Slide Carousel", 
                        "🐦 Twitter Thread", 
                        "📝 Static Post"
                    ])
                    
                    with tab1:
                        st.markdown("### Reel Script (20-30s)")
                        st.markdown(data.get("reel_script", ""))
                        
                    with tab2:
                        st.markdown("### 6-Slide Carousel")
                        st.markdown(data.get("carousel", ""))
                        
                    with tab3:
                        st.markdown("### X / Twitter Thread")
                        st.markdown(data.get("twitter_thread", ""))
                        
                    with tab4:
                        st.markdown("### Static Caption")
                        st.markdown(data.get("static_caption", ""))
                        
                except Exception as e:
                    st.error(f"An error occurred during generation: {e}")