# import streamlit as st
# from transformers import pipeline

# # Load a better-suited model (try different models if needed)
# try:
#     qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
# except Exception as e:
#     qa_pipeline = None  # Handle case where model fails to load

# # Function to rephrase user input if needed
# def format_query(user_input):
#     if not user_input.endswith("?"):
#         return f"What could be the cause of {user_input}?"
#     return user_input

# # Chatbot response function
# def chatbot_response(user_input):
#     formatted_query = format_query(user_input)

#     # Rule-based responses for common symptoms
#     if "headache" in user_input and "fever" in user_input and "7 days" in user_input:
#         return "Headache and fever lasting for several days might indicate flu or infection. See a doctor."

#     elif "headache" in user_input and "fever" in user_input:
#         return "A headache with fever may indicate flu, sinusitis, or an infection. Seek medical attention if symptoms persist."

#     else:
#         # Enhanced medical context
#         context = """
#         Common symptoms and potential causes:
#         - Sore throat + fever + cough: Cold, flu, or COVID-19.
#         - Stomach pain + nausea: Food poisoning, gastritis, or IBS.
#         - Wheezing + breathing difficulty: Asthma, allergy, or pneumonia.
#         - Fatigue + dizziness: Anemia, dehydration, or low blood pressure.
#         Consult a doctor if symptoms persist.
#         """
#         try:
#             if qa_pipeline:
#                 response = qa_pipeline(question=formatted_query, context=context)
#                 return response.get('answer', "I'm not sure. Please consult a doctor.")
#             else:
#                 return "AI model is unavailable. Try again later."
#         except Exception as e:
#             return f"Error: {e}"

# # Streamlit UI
# def main():
#     st.title("Medical Symptom Checker Chatbot 🤖")
#     st.write("Enter your symptoms or health-related questions, and the AI will assist you!")

#     user_input = st.text_input("Enter your symptoms or question:")

#     if user_input:
#         with st.spinner("Analyzing..."):
#             response = chatbot_response(user_input)
#             st.write("**AI Response:**", response)

#     st.write("---")
#     st.write("⚠️ **Note:** This chatbot is for informational purposes only. Always consult a doctor.")

# if __name__ == "__main__":
#     main()



import streamlit as st
from transformers import pipeline

# Load a more advanced model (Mistral 7B Instruct for better reasoning)
try:
    qa_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
except Exception as e:
    qa_pipeline = None  # Handle case where model fails to load

# Function to structure the query

def format_query(user_input):
    if not user_input.endswith("?"):
        return f"What could be the cause of {user_input}?"
    return user_input

# Chatbot response function
def chatbot_response(user_input):
    formatted_query = format_query(user_input)

    # Rule-based responses for common symptoms
    if "headache" in user_input and "fever" in user_input and "7 days" in user_input:
        return "Headache and fever lasting for several days might indicate flu or infection. See a doctor."

    elif "headache" in user_input and "fever" in user_input:
        return "A headache with fever may indicate flu, sinusitis, or an infection. Seek medical attention if symptoms persist."
    
    # AI-generated response
    context = """
    Common symptoms and potential causes:
    - Sore throat + fever + cough: Cold, flu, or COVID-19.
    - Stomach pain + nausea: Food poisoning, gastritis, or IBS.
    - Wheezing + breathing difficulty: Asthma, allergy, or pneumonia.
    - Fatigue + dizziness: Anemia, dehydration, or low blood pressure.
    Consult a doctor if symptoms persist.
    """
    
    try:
        if qa_pipeline:
            response = qa_pipeline(formatted_query + "\n\n" + context, max_length=200, num_return_sequences=1)
            return response[0]['generated_text']
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



