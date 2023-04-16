import gradio as gr
import openai
import sqlite3




openai.api_key = "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"


messages = [{"role": "system", "content": "You are a data scientist and a doctor which takes parameters listed as input and output top5 most probabble fatal diseases to be contracted and top 5 possible allergies to medications in future based on data from patients with similar medical history also recommend other top 5 Lab test that should be done for prevention and early diagnosis of diseases give top5 most probabble illnesses with percent chance also give top5 vaccines for diseases currently spreading also give list of top5 medicine salts also Predict the likelihood of a patient being readmitted to the hospital after being discharge"}]
def store_data(name ,aadhaar,age, gender, diagnosis, lab_results, symptoms, past_problems):
    # Connect to the database
    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS health_data
                 (name TEXT,aadhaar TEXT,age TEXT, gender TEXT, diagnosis TEXT,
                 lab_results TEXT, symptoms TEXT,
                  past_problems TEXT)''')

    # Insert the data into the table
    c.execute("INSERT INTO health_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (name,aadhaar,age, gender, diagnosis,
               lab_results, symptoms,
            past_problems))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
def CustomChatGPT(Name, Aadhaar, Age,Gender,Diagnosis,Symptoms,Pastproblems,labresults):
    store_data(Name,Aadhaar,Age, Gender, Diagnosis,Symptoms,Pastproblems,labresults
               )
    labr = labresults.split(',')
    lab_results = {}
    for item in labr:
        key, value = item.split(':')
        lab_results[key] = value
    symptoms = Symptoms.split(',')
    past_problems = Pastproblems.split(',')

    user_input = f"The patient is a {Age}-year-old {Gender} with {Diagnosis}. Lab results show{labresults} . Symptoms include {', '.join(symptoms)} and past problems include {', '.join(past_problems)}."
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
    print(ChatGPT_reply)
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs=["text", "text", "text","text","text","text", "text", "text"],
    outputs=["text"],
)
# CustomChatGPT(user_input)
demo.launch(share=True)