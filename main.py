import openai
import gradio
import config

openai.api_key = config.OPENAI_KEY
messages = [{"role": "system", "content": "You are a therapist and friend to a University student"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

theme_red = gradio.themes.Soft(
    primary_hue="red",
    secondary_hue="red",
)

demo = gradio.Interface(theme=theme_red,
                        fn=CustomChatGPT, 
                        inputs="text", 
                        outputs="text", 
                        title="TerrapinTalk")

demo.launch(share=True)
