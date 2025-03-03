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

# Load a different model (DistilBERT for QA tasks)
try:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
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
    if "headache" in user_input:
        return ("A headache that doesn't improve with painkillers may have multiple causes, including:\n"
                "- **Migraines**: Often with nausea, sensitivity to light, and visual disturbances.\n"
                "- **Tension Headaches**: Stress-related pain, like a band tightening around the head.\n"
                "- **Sinus Headache**: Pressure due to sinus infections, often with nasal congestion.\n"
                "- **Caffeine Withdrawal**: Cutting down on caffeine can trigger headaches.\n"
                "- **Dehydration**: Lack of fluids can cause persistent headaches.\n"
                "- **High Blood Pressure**: Severe hypertension may result in pounding headaches.\n"
                "- **Serious Conditions (Seek urgent care if you experience):**\n"
                "  - **Brain Hemorrhage**: Sudden, severe headache with confusion, vision loss, or weakness.\n"
                "  - **Meningitis**: Stiff neck, fever, and sensitivity to light.\n"
                "\n🚨 **When to See a Doctor:**\n"
                "- If the headache is **sudden & severe (worst headache ever)**.\n"
                "- If it comes with **vomiting, confusion, or loss of consciousness**.\n"
                "- If it **lasts more than 72 hours** despite medication.")

    elif "joints ache" in user_input:
        return ("Joint pain without exercise could be caused by:\n"
                "- **Osteoarthritis**: Wear and tear on joints.\n"
                "- **Rheumatoid Arthritis**: An autoimmune disorder affecting joints.\n"
                "- **Gout**: Uric acid buildup causing sharp joint pain.\n"
                "- **Vitamin D Deficiency**: Can weaken bones and cause discomfort.\n"
                "- **Infections (e.g., Lyme Disease)**: Some bacterial infections trigger joint pain.\n"
                "\n🚨 **When to See a Doctor:**\n"
                "- If the pain is persistent, severe, or accompanied by swelling or redness.\n"
                "- If it's affecting multiple joints suddenly.")

    # AI-generated response
    context = """
    Common symptoms and potential causes:
    - Sore throat + fever + cough: Cold, flu, or COVID-19.
    - Stomach pain + nausea: Food poisoning, gastritis, or IBS.
    - Wheezing + breathing difficulty: Asthma, allergy, or pneumonia.
    - Fatigue + dizziness: Anemia, dehydration, or low blood pressure.
    - Severe headache that doesn’t go away with painkillers: Migraine, tension headache, brain hemorrhage, or meningitis. Seek medical attention if persistent.
    Consult a doctor if symptoms persist.
    """
    
    try:
        if qa_pipeline:
            response = qa_pipeline(question=formatted_query, context=context)
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




