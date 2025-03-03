import streamlit as st
from transformers import pipeline

# Load the model (lightweight yet effective)
try:
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
except Exception as e:
    qa_pipeline = None  # Handle case where model fails to load

# Function to structure the query
def format_query(user_input):
    if not user_input.endswith("?"):
        return f"What could be the cause of {user_input}?"
    return user_input

# Medical knowledge base
medical_context = """
Possible causes for common symptoms:
- Severe headache + no relief from painkillers: Migraine, brain hemorrhage, or meningitis.
- Persistent joint pain without exercise: Rheumatoid arthritis, osteoarthritis, or autoimmune disease.
- Fatigue + dizziness: Anemia, dehydration, heart issues, or low blood pressure.
- Sore throat + fever + cough: Cold, flu, strep throat, or COVID-19.
- Stomach pain + nausea: Food poisoning, gastritis, IBS, or acid reflux.
- Shortness of breath + wheezing: Asthma, pneumonia, or heart failure.
- Chest pain + left arm numbness: Possible heart attack, see a doctor immediately.
- Swollen feet + fatigue: Kidney disease, heart failure, or poor circulation.
Consult a doctor if symptoms persist.
"""

# Chatbot response function
def chatbot_response(user_input):
    formatted_query = format_query(user_input)

    try:
        if qa_pipeline:
            response = qa_pipeline(question=formatted_query, context=medical_context)
            return response['answer']
        else:
            return "AI model is unavailable. Try again later."
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
def main():
    st.title("🩺 Medical Symptom Checker Chatbot 🤖")
    st.write("Enter your symptoms or health-related questions, and the AI will assist you!")

    user_input = st.text_input("Enter your symptoms or question:")

    if user_input:
        with st.spinner("Analyzing..."):
            response = chatbot_response(user_input)
            st.write("**AI Response:**", response)

    st.write("---")
    st.warning("⚠️ **Note:** This chatbot is for informational purposes only. Always consult a doctor.")

if __name__ == "__main__":
    main()
