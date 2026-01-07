"""
Voice of the Doctor Module
Handles Text-to-Speech (TTS) functionality for converting doctor's responses into audio.

Available TTS options:
1. gTTS (Google Text-to-Speech) - Online, high quality
2. pyttsx3 - Offline, lower quality but doesn't require internet
"""

import os
import subprocess
import platform
from gtts import gTTS
import pyttsx3


# ============================================================================
# MAIN TTS FUNCTIONS - Use these in your application
# ============================================================================

def text_to_speech_with_gtts(input_text, output_filepath="doctor_response.mp3", auto_play=False):
    """
    Converts text to speech using Google Text-to-Speech (gTTS) and saves as MP3.
    Optionally plays the audio automatically.
    
    Args:
        input_text (str): The text to convert to speech
        output_filepath (str): Path where the MP3 file will be saved
        auto_play (bool): If True, automatically plays the audio after saving
    
    Returns:
        str: Path to the saved audio file
        
    Raises:
        Exception: If audio generation or playback fails
    """
    try:
        # Generate audio using gTTS
        language = "en"
        audioobj = gTTS(
            text=input_text,
            lang=language,
            slow=False
        )
        audioobj.save(output_filepath)
        print(f"[gTTS] Audio saved to {output_filepath}")
        
        # Auto-play if requested
        if auto_play:
            _play_audio(output_filepath)
            
        return output_filepath
        
    except Exception as e:
        print(f"[gTTS ERROR] Failed to generate audio: {e}")
        raise


def text_to_speech_with_pyttsx3(input_text, output_filepath="doctor_response.mp3", auto_play=False):
    """
    Converts text to speech using pyttsx3 (offline TTS) and saves as MP3.
    Optionally plays the audio automatically.
    
    Args:
        input_text (str): The text to convert to speech
        output_filepath (str): Path where the MP3 file will be saved
        auto_play (bool): If True, automatically plays the audio after saving
    
    Returns:
        str: Path to the saved audio file
        
    Raises:
        Exception: If audio generation or playback fails
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)   # speaking speed
        engine.setProperty('volume', 1.0) # max volume

        # Save audio to file
        engine.save_to_file(input_text, output_filepath)
        engine.runAndWait()
        print(f"[pyttsx3] Audio saved to {output_filepath}")
        
        # Auto-play if requested
        if auto_play:
            _play_audio(output_filepath)
            
        return output_filepath
        
    except Exception as e:
        print(f"[pyttsx3 ERROR] Failed to generate audio: {e}")
        raise


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _play_audio(audio_filepath):
    """
    Plays an audio file based on the operating system.
    
    Args:
        audio_filepath (str): Path to the audio file to play
        
    Raises:
        OSError: If the operating system is not supported
        Exception: If audio playback fails
    """
    os_name = platform.system()
    
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', audio_filepath], check=True)
        elif os_name == "Windows":  # Windows
            subprocess.run(
                ['powershell', '-c', f'(New-Object Media.SoundPlayer "{audio_filepath}").PlaySync();'],
                check=True
            )
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', audio_filepath], check=True)
        else:
            raise OSError(f"Unsupported operating system: {os_name}")
            
        print(f"[Audio Player] Successfully played: {audio_filepath}")
        
    except Exception as e:
        print(f"[Audio Player ERROR] Failed to play audio: {e}")
        raise


# ============================================================================
# TESTING / EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Test with sample text
    test_text = "Hello! I am your AI doctor assistant. How can I help you today?"
    
    print("\n=== Testing gTTS ===")
    try:
        text_to_speech_with_gtts(test_text, "test_gtts.mp3", auto_play=False)
        print("✅ gTTS test successful")
    except Exception as e:
        print(f"❌ gTTS test failed: {e}")
    
    print("\n=== Testing pyttsx3 ===")
    try:
        text_to_speech_with_pyttsx3(test_text, "test_pyttsx3.mp3", auto_play=False)
        print("✅ pyttsx3 test successful")
    except Exception as e:
        print(f"❌ pyttsx3 test failed: {e}")
    
    print("\n=== All tests complete ===")
