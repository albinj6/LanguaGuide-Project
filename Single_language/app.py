from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, MarianMTModel, MarianTokenizer
import torch

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Translator:
    def __init__(self):
        self.en_to_es_model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')
        self.es_to_en_model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-en')
        self.en_to_es_tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')
        self.es_to_en_tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-en')
    
    def translate(self, text, direction="en_to_es"):
        if direction == "en_to_es":
            inputs = self.en_to_es_tokenizer(text, return_tensors="pt", padding=True)
            translated = self.en_to_es_model.generate(**inputs)
            return self.en_to_es_tokenizer.decode(translated[0], skip_special_tokens=True)
        elif direction == "es_to_en":
            inputs = self.es_to_en_tokenizer(text, return_tensors="pt", padding=True)
            translated = self.es_to_en_model.generate(**inputs)
            return self.es_to_en_tokenizer.decode(translated[0], skip_special_tokens=True)

class BilingualChatbot:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        self.chat_tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.chat_model = AutoModelForCausalLM.from_pretrained(model_name)
        self.translator = Translator()
        self.chat_history_ids = None
    
    def get_response(self, user_input):
        new_user_input_ids = self.chat_tokenizer.encode(user_input + self.chat_tokenizer.eos_token, return_tensors='pt')
        if self.chat_history_ids is not None:
            bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1)
        else:
            bot_input_ids = new_user_input_ids
        
        self.chat_history_ids = self.chat_model.generate(
            bot_input_ids, max_length=1000, pad_token_id=self.chat_tokenizer.eos_token_id
        )
        
        bot_response_in_english = self.chat_tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        bot_response_in_spanish = self.translator.translate(bot_response_in_english, direction="en_to_es")
        user_input_in_spanish = self.translator.translate(user_input,direction="en_to_es")
        
        return bot_response_in_spanish, bot_response_in_english, user_input_in_spanish

chatbot = BilingualChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    response_spanish, response_english, input_spanish = chatbot.get_response(user_input)
    
    return jsonify({
        "response_spanish": response_spanish,
        "response_english": response_english,
        "input_spanish": input_spanish
    })


if __name__ == "__main__":
    app.run(debug=True)
