from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Load the tokenizer and model
model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = MBart50Tokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(r'https://drive.google.com/drive/folders/1-3j9JckERYkH6DlkZ75Jbn2Xb8D2mvUg?usp=sharing')

# Function for generating ISL glosses from English sentences
def generate_translation(english_sentence):
    # Tokenize input text
    inputs = tokenizer(english_sentence, return_tensors="pt", max_length=128, padding=True, truncation=True)

    # Generate translation
    output_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=128, early_stopping=True)

    # Decode the generated output
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text

# Example usage
if __name__ == '__main__':
    while True:
        user_input = input("Enter a sentence to translate (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            break
        isl_gloss = generate_translation(user_input)
        print(f"Input: {user_input}")
        print(f"ISL Gloss: {isl_gloss}")