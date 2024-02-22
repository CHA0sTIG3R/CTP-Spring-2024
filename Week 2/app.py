from flask import Flask, render_template, request
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

app = Flask(__name__)
client = OpenAI()

def generate_post(tone, topic, length, instructions):
    prompt = f"Write a {tone} blog post about {topic}. Make sure the blog post is no longer than {length} words and ends with a conclusion. {instructions}"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["In conclusion", "In summary"]
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_blog():
    # Retrieve form data
    topic = request.form.get('topic') 
    tone = request.form.get('tone')
    length = request.form.get('length')
    instructions = request.form.get('instructions')
    
    # Here, you would add your model inference code to generate the blog post
    generated_text = generate_post(tone, topic, length, instructions)

    return render_template('results.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
