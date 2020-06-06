#web_app/services/basilica_services.py
import basilica
import os
from dotenv import load_dotenv

load_dotenv() # parse the .env file for the environmental variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

#connection = basilica.Connection('a0a0c93b-f246-41bd-6f06-101e687ae06c')
connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ == "__main__":
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]