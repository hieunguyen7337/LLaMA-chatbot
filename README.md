# LLaMA Chatbot
## Description 
This is a Python program that creates a chatbot using the Huggingface LLaMA model. The chatbot is capable of responding to user input and continuing the conversation based on the context of the previous conversation. The chatbot use the LLaMA 7B model which has 7B parameters and is overall about 13GB. The model run in an 8bit configuration for faster inference.

## Requirements 
- Python 3.9

## Installation 
Run the 2 following command to install library and to download model weight

`bash installation.sh`

`bash download_model.sh`

## Usage
You can run the chatbot offline with running `chatbot-offline.py` file. 

<mark>Note! The model even in 8bit configuration with take about 8.6GB of your GPU RAM, is it recommended for your GPU to be in the 12-16GB range.</mark>

The user can input any text to start a conversation. The chatbot will respond to the user's input based on the context of the previous conversation. The conversation can be ended by typing "break" or restarted by typing "restart".

## Credits
This code uses the LLaMA 7B model from Hugging Face Transformers library, which is an open-source library for NLP models. The LLaMA model is developed by Meta and is an open source model that can rival GPT3-ChatGPT.