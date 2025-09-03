import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDIsIw5HuHSpT39xmCh2QERN8Pey-JLWh0")
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("PromptPilot: Gemini-Powered Answer Engine")
st.markdown("Ask me anything using Google's Gemini 2.5 Flash model!")

user_input = st.text_input("Enter your question:", "")

if st.button("Generate Answer"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            response = model.generate_content(user_input)
            st.success("Here is the answer:")
            st.write(response.text)
    else:
        st.warning("Please enter a question to get an answer.")
