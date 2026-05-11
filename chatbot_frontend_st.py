import streamlit as st
from chatbot_backend import graph
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Attractive emoji title
st.markdown("""
# 🚀 **NeuralMind AI** 🤖
##### Your 24/7 Intelligent Assistant
---
""")


with st.sidebar:
    st.header("📋 Chat Controls")
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state['message_history'] = []
        st.rerun()
    
    st.markdown("---")
    st.info("💡 **Tips:**\n- Type your message below\n- The AI remembers conversation context\n- Ask follow-up questions for better responses")
    
    st.markdown("---")
    st.caption("Developed by Ali Akbar 🟢🟡🔴")

config = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type your message here...')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = graph.invoke({'messages': [HumanMessage(content=user_input)]}, config=config)
    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)