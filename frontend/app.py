import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Simple AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input box
if user_input := st.chat_input("Say something..."):
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send message to backend
    try:
        res = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
        bot_reply = res.json().get("response", "No response from server.")
    except Exception as e:
        bot_reply = f"Error: {e}"

    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
