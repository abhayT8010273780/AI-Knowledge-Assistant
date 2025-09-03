# GenSpark: AI Knowledge Assistant
 * Built a Q&amp;A app using Google’s Gemini for real-time answers. Designed a modern UI in Streamlit with custom CSS. Added prompt handling, error checks, and interactive outputs. Improved response quality through prompt tuning and input validation. Deployed locally, with plans for cloud hosting.
 
 * Tech: Python, Streamlit, Gemini 2.5 Flash

  <h1 align="center">✨ PromptPilot ✨</h1>
<h3 align="center">🚀 Gemini-Powered Answer Engine built with Streamlit</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Google-Gemini-4285F4?logo=google" alt="Gemini">
  <img src="https://img.shields.io/github/license/your-username/promptpilot" alt="License">
</p>

<p align="center">
  PromptPilot is a sleek Q&A engine ⚡ powered by <b>Google Gemini 2.5 Flash</b>  
  with an elegant UI built using <b>Streamlit</b>.
</p>

---

## 🎯 Features
✅ Ask any question, get instant AI-generated answers  
✅ Powered by **Gemini 2.5 Flash** — fast & smart  
✅ Simple, minimal & interactive **Streamlit UI**  
✅ Easy setup & ready to deploy 🚀  

---

## 📸 Preview
<p align="center">
  <img src="https://user-images.githubusercontent.com/your-screenshot.png" alt="App Screenshot" width="600">
</p>

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/promptpilot.git
cd promptpilot

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key in app.py
genai.configure(api_key="YOUR_API_KEY")

# 5. Run the app
streamlit run app.py

