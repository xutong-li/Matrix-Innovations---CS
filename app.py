# import openai

# # Set the API key
# # openai.api_key = "YOUR_API_KEY_HERE"
# openai.api_key = "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"

# def chat(prompt):
#     # Use the GPT API to generate a response to the prompt
#     response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, temperature=0.5)

#     # Return the response as a string
#     return response.text

# # Test the chat function
# print(chat("Hello, how are you today?"))


import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
f = open("openai_api.txt", 'r')
my_api_key = f.read()
openai.api_key = my_api_key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Start chatting with Matrix Innovations chatbot:\n"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Maxtrix Innovations Chat Bot</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)