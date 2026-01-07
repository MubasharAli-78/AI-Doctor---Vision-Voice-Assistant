"""
Voice of the Patient Module
Handles Speech-to-Text (STT) functionality for converting patient's voice input into text.

Features:
- Record audio from microphone
- Save audio as MP3 format
- Convert audio to text using Google Speech Recognition
- Support for both live recording and file-based conversion
"""

import logging
import os
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


FFMPEG_PATH = r"C:\Cffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\Cffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffprobe.exe"

if os.path.exists(FFMPEG_PATH):
    AudioSegment.converter = FFMPEG_PATH
    AudioSegment.ffprobe = FFPROBE_PATH
else:
    print(f"Warning: FFmpeg not found at {FFMPEG_PATH}")
    print("Audio recording may not work. Please install FFmpeg.")



logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)



def record_audio(mp3_path="patient_voice.mp3", record_seconds=6, mic_index=None):
    """
    Records audio from the microphone and saves it as an MP3 file.
    
    Args:
        mp3_path (str): Path where the MP3 file will be saved
        record_seconds (int): Duration to record in seconds
        mic_index (int): Microphone device index (None = default microphone)
    
    Returns:
        sr.AudioData: Audio data object that can be used for speech recognition
        None if recording fails
    """
    recognizer = sr.Recognizer()
    
    # Configure recognizer for better quality
    recognizer.pause_threshold = 999999  # Don't stop on pauses
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = False

    try:
        with sr.Microphone(device_index=mic_index) as source:
            logging.info("🎤 Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            logging.info(f"Recording for {record_seconds} seconds... Start speaking now!")
            audio = recognizer.record(source, duration=record_seconds)
            logging.info("Recording complete.")

        # Convert WAV bytes to MP3 format
        wav_bytes = audio.get_wav_data()
        sound = AudioSegment.from_wav(BytesIO(wav_bytes))
        sound = sound.normalize()  # Normalize audio levels
        sound.export(mp3_path, format="mp3", bitrate="192k")
        logging.info(f"💾 Audio saved to: {mp3_path}")

        return audio

    except Exception as e:
        logging.error(f"Recording error: {e}")
        return None


def speech_to_text(audio, language="en-US"):
    """
    Converts a speech_recognition AudioData object to text.
    
    Args:
        audio (sr.AudioData): Audio data from record_audio() or similar
        language (str): Language code (default: en-US)
    
    Returns:
        str: Transcribed text from the audio
    """
    recognizer = sr.Recognizer()
    
    try:
        text = recognizer.recognize_google(audio, language=language)
        logging.info(f"Transcription: {text}")
        return text
        
    except sr.UnknownValueError:
        logging.warning("Could not understand audio - please speak clearly")
        return "[Could not understand audio]"
        
    except sr.RequestError as e:
        logging.error(f"Recognition service error: {e}")
        return f"[Recognition service error: {e}]"


def convert_audio_file_to_text(audio_filepath, language="en-US"):
    """
    Converts an audio file (MP3, WAV, etc.) to text using Google Speech Recognition.
    This function is compatible with Gradio's audio output which provides a filepath.
    
    Args:
        audio_filepath (str): Path to the audio file
        language (str): Language code for recognition (default: en-US)
    
    Returns:
        str: Transcribed text from the audio file
        
    Examples:
        >>> text = convert_audio_file_to_text("patient_voice.mp3")
        >>> print(text)
        "I have a headache and fever"
    """
    recognizer = sr.Recognizer()
    
    # Validate file exists
    if not os.path.exists(audio_filepath):
        error_msg = f"[Error: Audio file not found: {audio_filepath}]"
        logging.error(f"{error_msg}")
        return error_msg
    
    try:
        # Load and process audio file
        logging.info(f"🎵 Loading audio file: {audio_filepath}")
        
        # speech_recognition requires WAV format, so convert if needed
        if audio_filepath.endswith('.mp3'):
            # Convert MP3 to WAV in memory
            sound = AudioSegment.from_mp3(audio_filepath)
            wav_path = audio_filepath.replace('.mp3', '_temp.wav')
            sound.export(wav_path, format='wav')
            
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
            
            # Clean up temporary WAV file
            if os.path.exists(wav_path):
                os.remove(wav_path)
        else:
            # Assume it's already WAV or compatible format
            with sr.AudioFile(audio_filepath) as source:
                audio_data = recognizer.record(source)
        
        # Convert to text
        text = recognizer.recognize_google(audio_data, language=language)
        logging.info(f"Transcription: {text}")
        return text
    
    except sr.UnknownValueError:
        logging.warning("Could not understand audio - please speak clearly")
        return "[Could not understand audio]"
        
    except sr.RequestError as e:
        error_msg = f"[Recognition service error: {e}]"
        logging.error(f"{error_msg}")
        return error_msg
        
    except Exception as e:
        error_msg = f"[Error processing audio file: {e}]"
        logging.error(f"{error_msg}")
        return error_msg


def record_and_transcribe(mp3_path="patient_voice.mp3", record_seconds=6, mic_index=None, language="en-US"):
    """
    Convenience function that records audio and immediately transcribes it.
    
    Args:
        mp3_path (str): Path where the MP3 file will be saved
        record_seconds (int): Duration to record in seconds
        mic_index (int): Microphone device index (None = default)
        language (str): Language code for recognition
    
    Returns:
        str: Transcribed text from the recorded audio
    """
    audio_obj = record_audio(mp3_path, record_seconds, mic_index)
    
    if audio_obj:
        return speech_to_text(audio_obj, language)
    else:
        return "[Recording failed]"




if __name__ == "__main__":
    print("\n" + "="*60)
    print("VOICE OF THE PATIENT - TEST MODE")
    print("="*60 + "\n")
    
    # Test 1: Record and transcribe
    print("Test 1: Recording and transcribing...")
    audio_obj = record_audio(
        mp3_path="patient_voice_test.mp3",
        record_seconds=5,
        mic_index=None
    )

    if audio_obj:
        transcribed_text = speech_to_text(audio_obj)
        print(f"\nResult: {transcribed_text}\n")
    else:
        print("\nRecording failed\n")
    
    print("="*60)
    print("🏁 Test complete")
    print("="*60 + "\n")
