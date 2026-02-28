# import streamlit as st
# import requests

# st.set_page_config(page_title="Tiny Content Machine", layout="wide")
# st.title("⚙️ The Tiny Content Machine")
# st.markdown("Turn one piece of long-form content into platform-native assets.")

# source_text = st.text_area("Paste your blog, article, or transcript here:", height=200)

# if st.button("Generate Content Engine", type="primary"):
#     if not source_text.strip():
#         st.warning("Please enter some text first.")
#     else:
#         with st.spinner("Agents are analyzing voice and generating platforms in parallel..."):
#             try:
#                 # Call the FastAPI backend
#                 response = requests.post(
#                     "http://localhost:8000/generate",
#                     json={"source_text": source_text}
#                 )
#                 response.raise_for_status()
#                 data = response.json()
                
#                 st.success("Content generation complete!")
                
#                 with st.expander("Detected Brand Voice & Tone (Click to expand)"):
#                     st.write(data["brand_voice"])
                
#                 tab1, tab2, tab3, tab4 = st.tabs([
#                     "📱 Instagram Reel", 
#                     "🎠 6-Slide Carousel", 
#                     "🐦 Twitter Thread", 
#                     "📝 Static Post"
#                 ])
                
#                 with tab1:
#                     st.markdown("### Reel Script (20-30s)")
#                     st.markdown(data["reel_script"])
                    
#                 with tab2:
#                     st.markdown("### 6-Slide Carousel")
#                     st.markdown(data["carousel"])
                    
#                 with tab3:
#                     st.markdown("### X / Twitter Thread")
#                     st.markdown(data["twitter_thread"])
                    
#                 with tab4:
#                     st.markdown("### Static Caption")
#                     st.markdown(data["static_caption"])
                    
#             except requests.exceptions.RequestException as e:
#                 st.error(f"Error connecting to the backend. Make sure FastAPI is running. Details: {e}")


import os
import streamlit as st
import requests

st.set_page_config(page_title="Tiny Content Machine", layout="wide")
st.title("⚙️ The Tiny Content Machine")
st.markdown("Turn one piece of long-form content into platform-native assets.")

source_text = st.text_area("Paste your blog, article, or transcript here:", height=200)

if st.button("Generate Content Engine", type="primary"):
    if not source_text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Agents are analyzing voice and generating platforms in parallel..."):
            try:
                # 1. Look for a live URL, but fall back to localhost if running locally
                API_URL = os.getenv("API_URL", "http://localhost:8000")
                
                # 2. Call the FastAPI backend dynamically
                response = requests.post(
                    f"{API_URL}/generate",
                    json={"source_text": source_text}
                )
                response.raise_for_status()
                data = response.json()
                
                st.success("Content generation complete!")
                
                with st.expander("Detected Brand Voice & Tone (Click to expand)"):
                    st.write(data["brand_voice"])
                
                tab1, tab2, tab3, tab4 = st.tabs([
                    "📱 Instagram Reel", 
                    "🎠 6-Slide Carousel", 
                    "🐦 Twitter Thread", 
                    "📝 Static Post"
                ])
                
                with tab1:
                    st.markdown("### Reel Script (20-30s)")
                    st.markdown(data["reel_script"])
                    
                with tab2:
                    st.markdown("### 6-Slide Carousel")
                    st.markdown(data["carousel"])
                    
                with tab3:
                    st.markdown("### X / Twitter Thread")
                    st.markdown(data["twitter_thread"])
                    
                with tab4:
                    st.markdown("### Static Caption")
                    st.markdown(data["static_caption"])
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the backend at {API_URL}. Details: {e}")