from dotenv import load_dotenv, find_dotenv
import os
from openai import OpenAI
import json

load_dotenv(find_dotenv())


# Initialize the OpenAI API client
client = OpenAI()

# Define the prompt
tone = "formal"
topic = "artificial intelligence"
length = "500"
instructions = "You can use any information from the internet, but make sure to cite your sources."

prompt = f"Write a {tone} blog post about {topic}. Make sure the blog post is no longer than {length} words and ends with a conclusion. {instructions}"

# Generate text using GPT-3
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

# Print the generated text
print(response.choices[0].text.strip())
