from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

X_train = ["I've been waiting for a HuggingFace course my whole life.",
           "I hate this so much!",
           "Python is the best programming language ever!",
           "People who like to eat are always the best people.",
           "People are so mean these days.",]

result = classifier(X_train)
print(result)

batch = tokenizer(X_train, padding=True, truncation=True, return_tensors="pt")
print(batch)

with torch.no_grad():
    outputs = model(**batch)
    print(outputs)
    predictions = F.softmax(outputs.logits, dim=-1)
    print(predictions)
    predicted_class_indices = torch.argmax(predictions, dim=1)
    print(predicted_class_indices)


save_dir = 'save'
tokenizer.save_pretrained(save_dir)
model.save_pretrained(save_dir)

tokenizer = AutoTokenizer.from_pretrained(save_dir)
model = AutoModelForSequenceClassification.from_pretrained(save_dir)
