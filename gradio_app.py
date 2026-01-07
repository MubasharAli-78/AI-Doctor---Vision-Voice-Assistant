"""
AI Doctor Chatbot - Gradio Web Interface (Simplified Version)
Compatible with all Gradio versions
"""

import os
import gradio as gr

from brain_of_the_doctor import query_llm_with_image
from voice_of_the_patient import convert_audio_file_to_text
from voice_of_the_doctor import text_to_speech_with_gtts


# System prompt for the AI doctor
SYSTEM_PROMPT = """You are a professional medical doctor. I know you are an AI, but this is for educational purposes.

Analyze the image and the patient's question carefully. 

If you identify any medical concerns, provide a differential diagnosis and suggest appropriate remedies or next steps.

IMPORTANT INSTRUCTIONS:
- Do NOT use numbers, bullet points, or special characters in your response
- Your response should be in one continuous paragraph
- Always answer as if you are speaking to a real patient
- Do NOT say "In the image I see" - instead say "With what I see, I think you have..."
- Do NOT respond as an AI model or use markdown formatting
- Your answer should sound like an actual doctor speaking, not an AI bot
- Keep your answer concise (maximum 2-3 sentences)
- No preamble - start your answer immediately

Patient's question: """


def process_patient_input(audio_filepath, image_filepath):
    """Main processing function"""
    try:
        print("\n" + "="*60)
        print("Processing patient input...")
        print("="*60)
        
        # Convert audio to text
        patient_question = convert_audio_file_to_text(audio_filepath)
        print(f"Patient question: {patient_question}")
        
        # Get AI response
        full_prompt = SYSTEM_PROMPT + patient_question
        doctor_response = query_llm_with_image(full_prompt, image_filepath)
        print(f"Doctor's response: {doctor_response}")
        
        # Convert to speech
        audio_output = "doctor_response.mp3"
        text_to_speech_with_gtts(doctor_response, audio_output)
        
        print("="*60 + "\n")
        
        return patient_question, doctor_response, audio_output
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        return error_msg, error_msg, None


# Create Gradio interface
print("\n" + "="*60)
print("AI DOCTOR CHATBOT - STARTING...")
print("="*60 + "\n")

iface = gr.Interface(
    fn=process_patient_input,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Patient Voice Input"),
        gr.Image(type="filepath", label="Medical Image")
    ],
    outputs=[
        gr.Textbox(label="Your Question"),
        gr.Textbox(label="Doctor's Diagnosis", lines=5),
        gr.Audio(type="filepath", label="Doctor's Voice Response")
    ],
    title="AI Doctor - Vision & Voice Assistant",
    description="Upload a medical image and record your question to get an AI-powered medical assessment.\n\nDisclaimer: This is an educational tool only. Always consult a real healthcare professional."
)

if __name__ == "__main__":
    iface.launch(debug=True, share=False)
