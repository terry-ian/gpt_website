
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# 設定你的 API 金鑰
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

# 初始化 Gemini API 客戶端
genai.configure(api_key="AIzaSyD8OG39WRzCydCU2l6qOmqLJkldMbFmI9o")

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    # 使用 Google Gemini API 生成答案
    answer = generate_answer(question)

    return jsonify({'answer': answer})

def generate_answer(question):
    # 使用 Google Gemini API 來生成答案
    response = chat.send_message(question)
    #response = model.generate_content(question)
    return response.text.replace('**','').replace('*','-')

if __name__ == '__main__':
    app.run(debug=True)
