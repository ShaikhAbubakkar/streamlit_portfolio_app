import streamlit as st
import openai


st.title("Tera Bhai!")

openai.api_key = st.secrets['OPENAI_API_KEY']

if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("What is up?"):
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ''

        try:
            for response in openai.ChatCompletion.create(
                model=st.session_state['openai_model'],
                messages=[
                    {'role': m['role'], 'content': m['content']}
                    for m in st.session_state.messages
                ],
                stream=True
            ):
                if 'choices' in response and response['choices']:
                    full_response += response['choices'][0]['delta'].get('content', '')
                    message_placeholder.markdown(full_response + "| ")
        except openai.error.RateLimitError:
            st.error("Rate limit exceeded. Please check your API usage and try again later.")
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred: {e}")

        message_placeholder.markdown(full_response)
    st.session_state.messages.append({'role': 'assistant', 'content': full_response})
