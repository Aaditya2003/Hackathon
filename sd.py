import openai
import gradio as gr


openai.api_key = "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"
#name
#adhaar

age = 35
gender = "male"
diagnosis = "Alzheimer"
lab_results = {
    "glucose": 250,
    "cholesterol": 235,
    "triglycerides": 150
}
symptoms = ["nausea", "stomach ache"]
past_problems = ["asthma"]
user_input = f"The patient is a {age}-year-old {gender} with {diagnosis}. Lab results show glucose level of {lab_results['glucose']}, cholesterol level of {lab_results['cholesterol']}, and triglycerides level of {lab_results['triglycerides']}. Symptoms include {', '.join(symptoms)} and past problems include {', '.join(past_problems)}."

messages = [{"role": "system", "content": "You are a data scientist and a doctor which takes parameters listed as input and output top5 most probabble fatal diseases to be contracted and top 5 possible allergies to medications in future based on data from patients with similar medical history also recommend other top 5 Lab test that should be done for prevention and early diagnosis of diseases give top5 most probabble illnesses with percent chance also give top5 vaccines for diseases currently spreading also give list of top5 medicine salts also Predict the likelihood of a patient being readmitted to the hospital after being discharge"}]

def CustomChatGPT(userin):
    messages.append({"role": "user", "content": userin})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    print(ChatGPT_reply)
CustomChatGPT(user_input)
