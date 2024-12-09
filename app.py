# Install required libraries (if running locally, comment this out when deployed)
# !pip install transformers torch streamlit

import streamlit as st
from transformers import pipeline

# Load the Hugging Face pipeline (ensure you authenticate with Hugging Face if needed)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Define the chatbot response function
def chatbot_response(user_input):
    # Define specific rules for certain inputs
    if "headache" in user_input and "fever" in user_input and "7 days" in user_input:
        return "Headache and fever lasting for several days might be the flu or a bacterial infection. It is important to consult a doctor for further examination."
    
    elif "headache" in user_input and "fever" in user_input:
        return "A headache with fever could be a cold, flu, or sinusitis. If symptoms persist, consider seeing a doctor."
    
    else:
        # Default behavior using Hugging Face model
        context = """
        Feeling sick could indicate a variety of issues. For example:
        - If you're experiencing sore throat, fever, and cough, it might be cold or flu.
        - If you're having trouble breathing and wheezing, it might be asthma or an allergy.
        - Stomach aches and nausea could be signs of food poisoning or IBS.
        If symptoms persist or worsen, see a doctor.
        """
        try:
            response = qa_pipeline(question=user_input, context=context)
            return response['answer']
        except Exception as e:
            return f"Error occurred: {e}"

# Streamlit UI
def main():
    st.title("Medical Symptom Checker Chatbot 🤖")
    st.write("Enter your symptoms or health-related questions, and the AI will assist you!")

    # User input box
    user_input = st.text_input("Enter your symptoms or question:")

    # Process input and display response
    if user_input:
        with st.spinner("Analyzing..."):
            response = chatbot_response(user_input)
            st.write("**AI Response:**", response)

    # Footer
    st.write("---")
    st.write("⚠️ **Note:** This chatbot is for informational purposes only. Consult a doctor for medical advice.")

if __name__ == "__main__":
    main()

