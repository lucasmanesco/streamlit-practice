import openai
import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv

load_dotenv('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')

openai.api_key = os.environ.get('API_KEY')


def generate_response(prompt):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
    )
    message = completion.choives[0].text
    return message

st.title('ChatGPT-like Web App')

if 'generated' not in st.session_state:
    st.session_state['generetade'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input('You: ', key='input')

if user_input:
    output=generate_response(user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
