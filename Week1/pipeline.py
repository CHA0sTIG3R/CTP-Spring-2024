from transformers import pipeline

classifier = pipeline('sentiment-analysis')

result = classifier('We are very happy to show you the huggingface Transformers library.')
print(result)


generator = pipeline('text-generation', model='distilgpt2')

result = generator('In this course, we will teach you how to', 
                   max_length=30, num_return_sequences=2)
print(result)


classifier1 = pipeline('zero-shot-classification')

result = classifier1(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

print(result)