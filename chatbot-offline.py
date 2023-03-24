from transformers import LLaMATokenizer, LLaMAForCausalLM, GenerationConfig

class LLaMA_Chatbot():
    def __init__(self):
        Initialize the tokenizer, model configuration and model using the GPT2 pre-trained model from Hugging Face Transformers
        self.tokenizer = LLaMATokenizer.from_pretrained("./LLaMa-7B-model") 
        self.model = LLaMAForCausalLM.from_pretrained("./LLaMa-7B-model",
                                                      load_in_8bit=True,
                                                      device_map="auto")

    def tokenize_text(self, text):
        inputs = tokenizer(text, return_tensors="pt")
        input_ids = inputs["input_ids"].cuda()
        return input_ids

    def model_generate_token(self, input_ids):
        generation_config = GenerationConfig(temperature=0.6,
                                             top_p=0.95,
                                             repetition_penalty=1.2)
        generation_output = model.generate(input_ids=input_ids,
                                           generation_config=generation_config,
                                           max_new_tokens=len(input_ids))
        return generation_output

    def model_generate(self, input_text):
        input_ids = self.tokenize_text(input_text)
        while(True):
            model_output = self.model_generate_token(input_ids)
            decoded_text = tokenizer.decode(model_output[0][-1:])
            print(decoded_text,end="")
            input_text += decoded_text
            if model_output[0][-1:] == 13:
                break
            input_ids = model_output
        return input_text

    def start_chat(self):
        print("""This is a chatbot create using the Huggingface opensource LLaMA 7B model, you can type in
break to stop the chatbot or restart to restart the chatbot conversation""")
        # Start the chatbot
        start = True
        while(True):
            if start:
                # initialize the chatbot with a starting prompt
                starting_prompt = """You are a chatbot, response to the user question as below."""
                context = starting_prompt 
                start = False
            else:
                context = output_text
            
            inp = input("User: ")
            # Allow the user to break out of the conversation or restart it
            if inp == "break":
                print("Goodbye")
                break
            if inp == "restart":
                print("----------------------------")
                start = True
                continue

            input_text = context + f"\nUser: {inp}\nChatbot:"
            output_text = self.model_generate(input_text)

if __name__ == '__main__':
    # Create an instance of the Chatbot class and start the chat
    chatbot = LLaMA_Chatbot()
    chatbot.start_chat()