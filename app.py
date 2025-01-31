import streamlit as st
import os
from groq import Groq  # Import Groq API
from langchain_core.messages import HumanMessage, AIMessage  # For handling message types
from langchain_groq import ChatGroq  # Import LangChain's Groq chat integration
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # For creating chat prompts
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.environ['GROQ_API_KEY']  # Retrieve Groq API key

def get_chat_response(chat, messages, user_input):
    """Get response from the chat model"""
    # Define the conversation prompt template
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="history"),  # Placeholder for past messages
        ("human", "{input}")  # User's latest input
    ])
    
    # Prepare message history (last 5 messages for context)
    message_history = []
    for msg in messages[-5:]:  # Limit history to last 5 messages
        if isinstance(msg, dict):
            if msg["role"] == "human":
                message_history.append(HumanMessage(content=msg["content"]))
            else:
                message_history.append(AIMessage(content=str(msg["content"])))
    
    # Create the chain by combining the prompt and chat model
    chain = prompt | chat
    response = chain.invoke({
        "history": message_history,  # Provide message history
        "input": user_input  # User's current input
    })
    
    # Extract just the response content
    if hasattr(response, 'content'):
        return response.content
    elif isinstance(response, str):
        return response
    else:
        return str(response)

def main():
    st.title("Groq Chat App")  # Streamlit app title
    
    # Sidebar configuration
    st.sidebar.title('Select an LLM')  # Sidebar title
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']  # Model options
    )
    memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)  # Memory length slider
    
    # Initialize the chat model
    chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model  # Use selected model
    )
    
    # Initialize session state for storing message history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history (limit to memory length)
    for message in st.session_state.messages[-memory_length:]:
        role = message.get("role", "assistant")
        content = message.get("content", "")
        if role == "human":
            st.write("You:", content)
        else:
            st.write("Chatbot:", content)
    
    # Input box for user question
    user_question = st.text_area("Ask a question:")
    
    if user_question:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "human",
            "content": user_question
        })
        
        try:
            # Get model response
            response = get_chat_response(chat, st.session_state.messages, user_question)
            
            # Add AI response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })
            
            # Display chatbot response
            st.write("Chatbot:", response)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")  # Display error message
            # Remove the failed message from history
            if st.session_state.messages:
                st.session_state.messages.pop()

# Run the Streamlit app
if __name__ == "__main__":
    main()
