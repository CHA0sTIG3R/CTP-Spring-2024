from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Set the device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate text
def generate_text(prompt, max_length=200, temperature=0.7, num_return_sequences=1):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    output = model.generate(
        input_ids=input_ids,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.5,
        do_sample=True,
    )
    decoded_output = [tokenizer.decode(ids, skip_special_tokens=True) for ids in output]
    return decoded_output

# Example prompt
prompt = "In today's world, artificial intelligence is..."

# Generate text
generated_text = generate_text(prompt)

# Display generated text
for i, text in enumerate(generated_text):
    print(f"Generated Text {i+1}:")
    print(text)
    print()

# Compare generated text with reference text or human-written examples
# Calculate accuracy metrics, e.g., BLEU score, ROUGE score, etc.
# You may need a set of reference texts or human-written examples for evaluation
