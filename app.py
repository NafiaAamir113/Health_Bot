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

# Load a reliable Q&A model
try:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
except Exception as e:
    st.error(f"Error loading AI model: {e}")
    qa_pipeline = None

# Rule-based responses for accurate symptom matching
def rule_based_response(user_input):
    symptoms = user_input.lower()

    if "severe headache" in symptoms and "doesn’t go away" in symptoms and "painkillers" in symptoms:
        return "A severe headache that doesn’t respond to painkillers may indicate a **migraine, tension headache, brain hemorrhage, or meningitis**. If persistent, seek medical attention immediately."

    elif "headache" in symptoms and "fever" in symptoms and "7 days" in symptoms:
        return "A **long-lasting headache with fever** may indicate **serious infection, meningitis, or another underlying condition**. Seek medical help."

    elif "headache" in symptoms and "fever" in symptoms:
        return "A headache with fever may indicate **flu, sinusitis, or infection**. Monitor symptoms and consult a doctor."

    elif "chest pain" in symptoms and "breathing difficulty" in symptoms:
        return "Chest pain with breathing difficulty can be **serious (heart attack, pulmonary embolism, or pneumonia)**. **Seek emergency care.**"

    elif "nausea" in symptoms and "vomiting" in symptoms and "stomach pain" in symptoms:
        return "Nausea, vomiting, and stomach pain could be due to **food poisoning, gastritis, or an ulcer**. If severe, consult a doctor."

    return None  # If no rule-based match, use AI

# AI-generated response function
def chatbot_response(user_input):
    rule_based = rule_based_response(user_input)
    if rule_based:
        return rule_based  # Return immediate response if a rule-based match exists

    formatted_query = user_input.strip() + "?"

    context = """
    Possible causes of common symptoms:
    - **Severe headache that doesn’t go away**: **Migraine, tension headache, brain hemorrhage, meningitis.**
    - **Sore throat + fever + cough**: Could be **cold, flu, strep throat, or COVID-19.**
    - **Stomach pain + nausea**: Could be **food poisoning, gastritis, or IBS.**
    - **Chest pain + shortness of breath**: May be **heart attack, asthma, or anxiety attack.**
    - **Fatigue + dizziness**: Possible **anemia, low blood pressure, dehydration.**
    - **Joint pain + swelling**: Could be **arthritis, gout, autoimmune disorder.**
    **Always consult a doctor for a professional diagnosis.**
    """

    try:
        if qa_pipeline:
            response = qa_pipeline(question=formatted_query, context=context)
            return response.get('answer', "I'm not sure. Please consult a doctor.")
        else:
            return "AI model is unavailable. Try again later."
    except Exception as e:
        return f"Error generating response: {e}"

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



