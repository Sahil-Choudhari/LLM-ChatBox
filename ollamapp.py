import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 'You are a helpful assistant, please respond to the questions asked.'),
        ("user", "Question: {Question}")
    ]
)

st.title("LangChain Demo Chat App with Gemma2:2b")
input_text = st.text_input('Write Your prompt:')


llm = Ollama(model="gemma2:2b")


# Run the chain when user inputs text
if input_text:
    formatted_prompt = [f"Question:{input_text}"]
    response = llm.generate(formatted_prompt)
    llm_text = response.generations[0][0].text
    st.write(llm_text)

print("Hello")
