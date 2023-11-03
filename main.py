import openai
import gradio
import config

messages = [{"role": "system", "content": "You are a psychologist and friend of a University student who is seeking mental health support."}]

def CustomChatGPT(user_input):
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply

app = gradio.Interface(fn=CustomChatGPT, inputs = "Input", outputs = "reponse", title = "TerrapinTalk", description = "A chatbot that provides mental health support to University of Maryland students.")

app.launch()