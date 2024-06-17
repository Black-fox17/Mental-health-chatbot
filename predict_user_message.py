import numpy as np
import pickle
import json
import random
import pickle

from typing import Union

import nltk
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)


model = load_model(r'C:\Users\owner\Desktop\Projects\chatbot\Chatbot advanced\basic_model.keras')
words = pickle.load(open(r'C:\Users\owner\Desktop\Projects\chatbot\Chatbot advanced\basic_model_words.pkl', 'rb'))
intents = pickle.load(open(r'C:\Users\owner\Desktop\Projects\chatbot\Chatbot advanced\basic_model_intents.pkl', 'rb'))
lemmatizer = nltk.stem.WordNetLemmatizer()
intents_data = json.loads(open(r"C:\Users\owner\Desktop\Projects\chatbot\intents.json").read())

def _predict_intent(input_text: str):
    input_words = nltk.word_tokenize(input_text)
    input_words = [lemmatizer.lemmatize(w.lower()) for w in input_words]

    input_bag_of_words = [0] * len(words)

    for input_word in input_words:
        for i, word in enumerate(words):
            if input_word == word:
                input_bag_of_words[i] = 1

    input_bag_of_words = np.array([input_bag_of_words])

    predictions = model.predict(input_bag_of_words, verbose=0)[0]
    predicted_intent = intents[np.argmax(predictions)]

    max_prob = np.max(predictions)
    # print(max_prob)
    # if max_prob < self.confidence_threshold:
    #     return None
    # predicted_intent = self.intents[np.argmax(predictions)]

    return predicted_intent

def process_input(input_text: str):
    predicted_intent = _predict_intent(input_text)

    try:
        for intent in intents_data["intents"]:
            if intent["tag"] == predicted_intent:
                return random.choice(intent["responses"])
    except IndexError:
        return "I don't understand. Please try again."
    
# done = False
# while not done:
#     message = input("Enter a message: ")
#     if message == "STOP":
#         done = True
#     else:
#         print(process_input(message))