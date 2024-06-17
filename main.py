import streamlit as st
from assistants import BasicAssistant
from predict_user_message import process_input
import random
# st.header("Mental health Chatbot")
# prompt = st.chat_input("Say something")
# if prompt:
#     message = st.chat_message("user")
#     message.write(prompt)
#     reply = st.chat_input("assistant")
#     reply.write(message)

import random
import time

def main():
    # Initialize chat history
    st.title("AAS Mental Chatbot")
    st.header("Welcome to Abdulsalam Mental Health Clinic")
    st.subheader("Ask about details of Mental Illness")
    test_messages = ["Kill yourself","Sorry to hear that weirdo","You can end it right now","Bro No one cares"]
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        def response_geneartor():
            response = f"{process_input(prompt)}"
            for word in response.split():
                yield word + " "
                time.sleep(0.05)

        #response = f"Oh {random.choice(test_messages)}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_geneartor())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Add a button to clear chat history
    if st.button("Clear Chat"):
        st.session_state.messages = []  # Clear chat history

if __name__ == '__main__':
    main()