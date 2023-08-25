import openai
import streamlit as st

openai.api_key= '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'

st.title("Chitchat Classification Chatbot")

text = st.text_input('Enter the text')

response=openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Classify following text as Chitchat or not , only answer in yes or no \n {text}",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


output=response['choices'][0]['text']


if st.button("Submit"):
        # Display bot's response
        if 'Yes' in output:
            bot_response = "It’s chitchat"
        else:
            bot_response = "It’s not chitchat"
        
        st.text("Bot:" + bot_response)