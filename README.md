# GenSpark: AI Knowledge Assistant
 * Built a Q&amp;A app using Google’s Gemini for real-time answers. Designed a modern UI in Streamlit with custom CSS. Added prompt handling, error checks, and interactive outputs. Improved response quality through prompt tuning and input validation. Deployed locally, with plans for cloud hosting.
 
 * Tech: Python, Streamlit, Gemini 2.5 Flash

   # 🚀 PromptPilot: Gemini-Powered Answer Engine

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?logo=streamlit)  
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)  
![Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4?logo=google)

**PromptPilot** is an interactive **Q&A application** built with [Streamlit](https://streamlit.io/) and powered by **Google's Gemini 2.5 Flash** model.  
Just type your question, and get an AI-generated answer instantly ⚡.

---

## ✨ Features
- 🔮 Ask anything — AI generates instant responses.
- 🎨 Clean and interactive UI using **Streamlit**.
- ⚡ Powered by **Gemini 2.5 Flash** for fast, intelligent answers.
- 🔑 Secure API key integration.

---

## 📂 Project Structure
📦 promptpilot
┣ 📜 app.py # Main Streamlit app
┣ 📜 requirements.txt # Dependencies
┗ 📜 README.md # Project documentation


---

## 🛠️ Installation & Setup

1. **Clone this repository**
   
   git clone https://github.com/your-username/promptpilot.git
   cd promptpilot
* Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
Install dependencies


pip install -r requirements.txt
Set your Gemini API key

Open app.py

Replace with your Gemini API key:


genai.configure(api_key="YOUR_API_KEY")
Run the app



Copy code
streamlit run app.py

