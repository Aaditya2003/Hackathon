import openai
import json

# Set up OpenAI API credentials
openai.api_key = "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"

# Define input parameters
age = 35
gender = "male"
diagnosis = "hypertension"
lab_results = {
    "glucose": 100,
    "cholesterol": 200,
    "triglycerides": 150
}
symptoms = ["headache", "fatigue"]
past_problems = ["asthma", "allergies"]

# Convert input parameters to text
input_text = f"The patient is a {age}-year-old {gender} with {diagnosis}. Lab results show glucose level of {lab_results['glucose']}, cholesterol level of {lab_results['cholesterol']}, and triglycerides level of {lab_results['triglycerides']}. Symptoms include {', '.join(symptoms)} and past problems include {', '.join(past_problems)}. give  most probabble illnesses with percent chance"

# Use GPT-3 API to generate output
response = openai.Completion.create(
  engine="davinci",
  prompt=input_text,
  max_tokens=1700,
  n=1,
  stop=None,
  temperature=0.5,
)

# Parse output
output_text = response.choices[0].text.strip()

# Print output
print(output_text)
