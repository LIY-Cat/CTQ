#server.py
from flask import Flask, render_template, request
import os
from openai import OpenAI

client = OpenAI(api_key='OPENAI_API_KEY')

#실행에 문제가 생겨서 잠시 제외
"""
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    )
"""

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/create_test_question', methods=['POST'])
def create_test_question():
    text = request.form['text']

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant."
            },
             {
                "role": "user", 
                "content": text
                }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #print(f'A: {response}')
    response_message = response.choices[0].message.content

    return render_template('main.html', response_message = response_message)


if __name__ == '__main__':
    #개발자용 서버라서 배포하면은 큰일남?
    #from waitress import serve
    app.run(debug=True, port=8000)
