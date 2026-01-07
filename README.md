# AI Doctor Chatbot - Vision & Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-Web%20Interface-orange)
![Google AI](https://img.shields.io/badge/Google-Gemini%20AI-green)
![License](https://img.shields.io/badge/License-Educational-yellow)

**An AI-powered medical assistant that combines voice input, image analysis, and voice output to provide medical assessments.**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [API Setup](#api-setup) • [Troubleshooting](#troubleshooting)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [API Setup](#api-setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Using the Web Interface](#using-the-web-interface)
  - [Testing Individual Modules](#testing-individual-modules)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [API Quota Management](#api-quota-management)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

AI Doctor Chatbot is an educational multimodal AI application that demonstrates the integration of:
- **Speech-to-Text (STT)** for patient voice input
- **Vision AI** for medical image analysis  
- **Large Language Models (LLM)** for intelligent diagnosis
- **Text-to-Speech (TTS)** for natural voice responses

This project showcases modern AI capabilities in a medical context while serving as a learning tool for developers interested in multimodal AI applications.

---

## Features

### Core Capabilities
- **Voice Input**: Record medical questions using your microphone
- **Image Analysis**: Upload and analyze medical images (skin conditions, wounds, etc.)
- **AI Diagnosis**: Powered by Google's Gemini AI for intelligent medical assessments
- **Voice Output**: Receive doctor's response in natural-sounding speech
- **Web Interface**: User-friendly Gradio-based interface

### Technical Features
- **Model Fallback**: Automatically switches between AI models if quota is exceeded
- **Error Handling**: Comprehensive error messages with helpful suggestions
- **Audio Processing**: MP3 format support with quality normalization
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Real-time Processing**: Fast response times with streaming support

---

## Architecture

The application consists of four main modules:

```
┌─────────────────────────────────────────────────────┐
│                   gradio_app.py                     │
│              (Web Interface & Orchestration)        │
└─────────────────────────────────────────────────────┘
         │                │                │
         ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   voice_of_  │  │  brain_of_   │  │  voice_of_   │
│   patient.py │  │  doctor.py   │  │  doctor.py   │
│              │  │              │  │              │
│ Speech-to-   │  │ Image        │  │ Text-to-     │
│ Text (STT)   │  │ Analysis     │  │ Speech (TTS) │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Module Descriptions

1. **gradio_app.py**: Main application that ties all components together
2. **brain_of_the_doctor.py**: Handles AI image analysis using Google Gemini
3. **voice_of_the_patient.py**: Converts patient's speech to text
4. **voice_of_the_doctor.py**: Converts AI responses to speech

---

## Prerequisites

Before installation, ensure you have:

- **Python 3.8 or higher**
- **FFmpeg** (for audio processing)
- **Google API Key** (for Gemini AI)
- **Microphone** (for voice input)
- **Internet Connection** (for API calls)

---

## Installation

### Windows

#### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/downloads/)

#### Step 2: Install FFmpeg
```bash
# Download FFmpeg from: https://ffmpeg.org/download.html
# Extract to: C:\Cffmpeg\ffmpeg-8.0.1-essentials_build\
# Or update the path in voice_of_the_patient.py
```

#### Step 3: Clone/Download the Project
```bash
# Navigate to the project directory
cd AI-DOCTOR-CHATBOT
```

#### Step 4: Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

#### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### macOS

#### Step 1: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Python and FFmpeg
```bash
brew install python ffmpeg
```

#### Step 3: Setup Virtual Environment
```bash
cd AI-DOCTOR-CHATBOT
python3 -m venv venv
source venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Linux

#### Step 1: Install Dependencies
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv ffmpeg portaudio19-dev

# Fedora
sudo dnf install python3 python3-pip ffmpeg portaudio-devel

# Arch
sudo pacman -S python python-pip ffmpeg portaudio
```

#### Step 2: Setup Virtual Environment
```bash
cd AI-DOCTOR-CHATBOT
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## API Setup

### Getting Your Google API Key

1. **Visit Google AI Studio**  
   Go to: [https://ai.google.dev/](https://ai.google.dev/)

2. **Sign In**  
   Use your Google account to sign in

3. **Create API Key**  
   - Click on "Get API Key"
   - Create a new project (or select existing)
   - Click "Create API Key"
   - Copy the generated key

4. **Add to Environment Variables**  
   Open the `.env` file in the project root and add:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

5. **Verify Setup**  
   The key should look like: `AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Important Notes
- Keep your API key private (never commit to Git)
- Free tier includes generous quotas for testing
- Monitor usage at: [https://ai.dev/usage](https://ai.dev/usage)

---

## Usage

### Running the Application

#### Start the Web Interface
```bash
python gradio_app.py
```

The application will start and display:
```
============================================================
AI DOCTOR CHATBOT - STARTING...
============================================================

* Running on local URL:  http://127.0.0.1:7860
```

#### Access the Interface
Open your web browser and navigate to:
```
http://localhost:7860
```

#### Stop the Application
Press `Ctrl + C` in the terminal

### Using the Web Interface

1. **Upload Medical Image**
   - Click on the "Medical Image" box
   - Select an image file (JPG, PNG, etc.)
   - Examples: skin conditions, wounds, rashes

2. **Record Your Question**
   - Click the microphone button
   - Speak clearly: "What's wrong with this image?"
   - Recording duration: 5-10 seconds

3. **Submit**
   - Click the "Submit" button
   - Wait for AI processing (5-15 seconds)

4. **Review Results**
   - **Your Question**: Transcribed text from your voice
   - **Doctor's Diagnosis**: AI analysis and recommendations
   - **Voice Response**: Click play to hear the diagnosis

### Testing Individual Modules

#### Test Speech-to-Text
```bash
python voice_of_the_patient.py
```
Speak when prompted and see the transcription.

#### Test Text-to-Speech
```bash
python voice_of_the_doctor.py
```
Generates test audio files.

#### Test Image Analysis
```bash
python brain_of_the_doctor.py
```
Requires a test image (e.g., `acne.jpg`) in the project directory.

---

## Configuration

### Changing the AI Model

Edit `brain_of_the_doctor.py`:
```python
def query_llm_with_image(query, image_path, model="gemini-2.5-flash"):
    # Change to: "gemini-1.5-pro" or "gemini-1.5-flash"
```

**Available Models:**
- `gemini-2.5-flash` - Latest, fastest (recommended)
- `gemini-1.5-flash` - Stable, good performance
- `gemini-1.5-pro` - Highest quality, slower

### Adjusting Recording Duration

Edit `voice_of_the_patient.py`:
```python
def record_audio(mp3_path="patient_voice.mp3", record_seconds=10):
    # Change record_seconds to desired duration
```

### Customizing System Prompt

Edit `gradio_app.py`:
```python
SYSTEM_PROMPT = """
Your custom instructions here...
"""
```

### Selecting Microphone

List available microphones:
```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```

Update in `voice_of_the_patient.py`:
```python
record_audio(mic_index=1)  # Change to your mic index
```

---

## Project Structure

```
AI-DOCTOR-CHATBOT/
│
├── brain_of_the_doctor.py      # Image analysis with Gemini AI
├── voice_of_the_patient.py     # Speech-to-Text processing
├── voice_of_the_doctor.py      # Text-to-Speech generation
├── gradio_app.py               # Main web application
│
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys)
├── .env.example                # Template for .env
├── README.md                   # This file
│
└── (generated files)
    ├── doctor_response.mp3     # AI voice response
    ├── patient_voice.mp3       # Recorded patient audio
    └── *.wav, *.mp3            # Temporary audio files
```

### File Descriptions

| File | Purpose | Key Functions |
|------|---------|---------------|
| `brain_of_the_doctor.py` | AI image analysis | `query_llm_with_image()` |
| `voice_of_the_patient.py` | Voice recording & STT | `record_audio()`, `convert_audio_file_to_text()` |
| `voice_of_the_doctor.py` | Text-to-speech | `text_to_speech_with_gtts()` |
| `gradio_app.py` | Web interface & orchestration | `process_patient_input()` |

---

## Troubleshooting

### Common Issues and Solutions

#### 1. "No module named 'dotenv'"
```bash
pip install python-dotenv
```

#### 2. "GOOGLE_API_KEY is missing"
- Create a `.env` file in the project root
- Add: `GOOGLE_API_KEY=your_key_here`
- Ensure no spaces around the `=`

#### 3. "FFmpeg not found"
**Windows:**
- Download from: [ffmpeg.org](https://ffmpeg.org)
- Update path in `voice_of_the_patient.py`

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

#### 4. "Could not understand audio"
- Speak clearly and loudly
- Reduce background noise
- Check microphone permissions
- Increase recording duration
- Test microphone in system settings

#### 5. "429 RESOURCE_EXHAUSTED"
This means you've exceeded your API quota.

**Solutions:**
- Wait 24 hours for quota reset
- Use a different Google account/API key
- The app automatically tries fallback models
- Check usage at: [https://ai.dev/usage](https://ai.dev/usage)

#### 6. "Gradio interface not loading"
- Ensure port 7860 is not in use
- Try a different port in `gradio_app.py`:
  ```python
  iface.launch(server_port=8080)
  ```
- Check firewall settings

#### 7. "Audio not playing"
- Check system audio settings
- Verify audio file was created
- Try manual playback of `doctor_response.mp3`

---

## API Quota Management

### Understanding Google API Quotas

**Free Tier Limits (Per Day):**
| Model | Requests/Min | Requests/Day | Input Tokens/Min |
|-------|--------------|--------------|------------------|
| gemini-2.5-flash | 15 | 1,500 | 1,000,000 |
| gemini-1.5-flash | 15 | 1,500 | 1,000,000 |
| gemini-1.5-pro | 2 | 50 | 32,000 |

### Smart Model Fallback

The application automatically tries multiple models if one exceeds quota:
1. First tries: Default model (gemini-2.5-flash)
2. If failed: Tries gemini-1.5-flash
3. If failed: Tries gemini-1.5-pro
4. If all fail: Shows helpful error message

### Monitoring Usage

Check your current usage:
- Visit: [https://ai.dev/usage?tab=rate-limit](https://ai.dev/usage?tab=rate-limit)
- Monitor daily and per-minute quotas
- Set up alerts for quota thresholds

### Best Practices

1. **Optimize Requests**
   - Don't spam the API
   - Wait a few seconds between requests
   - Use appropriate model for your needs

2. **Image Optimization**
   - Resize large images before upload
   - Use JPEG for better compression
   - Typical size: 500KB - 2MB

3. **Caching**
   - Consider caching similar queries
   - Store results locally when possible

4. **Upgrade Options**
   - Paid tier available at: [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
   - Significantly higher quotas
   - Better rate limits

---

## Disclaimer

### Medical Disclaimer

**THIS APPLICATION IS FOR EDUCATIONAL PURPOSES ONLY**

- This is NOT a medical diagnostic tool
- This is NOT a substitute for professional medical advice
- DO NOT use this application for actual medical decisions
- ALWAYS consult qualified healthcare professionals for medical concerns
- The AI may provide inaccurate or incomplete information

### Privacy Notice

- Audio recordings are processed via Google's Speech-to-Text API
- Images are sent to Google's Gemini AI for analysis
- No data is permanently stored by this application
- Review Google's privacy policy for their data handling practices
- Do not upload sensitive personal medical information

### Liability

The creators and contributors of this project:
- Accept no liability for medical decisions made using this tool
- Make no warranties about accuracy or reliability
- Recommend professional medical consultation for all health concerns

---

## Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment details

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide use cases and examples

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Open a pull request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/AI-DOCTOR-CHATBOT.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/  # If tests exist
```

---

## Dependencies

### Core Dependencies

- **python-dotenv** - Environment variable management
- **google-genai** - Google Gemini AI client
- **gradio** - Web interface framework
- **pillow** - Image processing
- **gtts** - Google Text-to-Speech
- **pyttsx3** - Offline Text-to-Speech
- **SpeechRecognition** - Speech-to-Text
- **pydub** - Audio file processing
- **pypiwin32** - Windows audio support (Windows only)

### Installing All Dependencies

```bash
pip install -r requirements.txt
```

### Updating Dependencies

```bash
pip install --upgrade -r requirements.txt
```

---

## License

This project is licensed for **Educational Use Only**.

### Terms of Use

- Free to use for learning and educational purposes
- Not licensed for commercial use
- Not licensed for actual medical practice
- Respect Google's API terms of service
- Respect all third-party library licenses

### Third-Party Licenses

This project uses several open-source libraries. Please review their licenses:
- Google Gemini AI: [Google Terms](https://ai.google.dev/terms)
- Gradio: [Apache License 2.0](https://github.com/gradio-app/gradio/blob/main/LICENSE)
- Other dependencies: See individual package licenses

---

## Acknowledgments

- **Google** for providing the Gemini API
- **Gradio** for the excellent web interface framework
- **Speech Recognition** community for STT capabilities
- **gTTS** developers for Text-to-Speech functionality
- All open-source contributors

---

## Support

### Getting Help

- **Documentation**: Read this README thoroughly
- **Issues**: Check [GitHub Issues](link-to-issues)
- **API Docs**: [Google AI Documentation](https://ai.google.dev/docs)
- **Gradio Docs**: [Gradio Documentation](https://gradio.app/docs)

### Contact

For questions or support:
- Open an issue on GitHub
- Check existing discussions
- Review troubleshooting section above

---

## Roadmap

Future improvements planned:

- [ ] Multi-language support
- [ ] Medical history tracking
- [ ] PDF report generation
- [ ] Integration with medical databases
- [ ] Advanced symptom checker
- [ ] Appointment scheduling
- [ ] Mobile app version
- [ ] Offline mode support
- [ ] Batch image processing
- [ ] Enhanced security features

---

## Changelog

### Version 1.0.0 (Current)
- Initial release
- Voice input and output
- Image analysis with Gemini AI
- Gradio web interface
- Model fallback for quota management
- Cross-platform support

---

<div align="center">

Made with ❤️ for educational purposes

**[⬆ Back to Top](#ai-doctor-chatbot---vision--voice-assistant)**

</div>
