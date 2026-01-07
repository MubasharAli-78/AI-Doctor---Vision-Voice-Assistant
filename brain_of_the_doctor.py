"""
Brain of the Doctor Module
Handles multimodal AI processing using Google's Gemini model.

Features:
- Vision + Language understanding
- Analyze medical images with text queries
- Powered by Google GenAI (Gemini 2.5 Flash)
"""

import os
from dotenv import load_dotenv
from google import genai
from PIL import Image


# ============================================================================
# ENVIRONMENT SETUP
# ============================================================================

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_google_api_key_here":
    raise ValueError(
        "❌ GOOGLE_API_KEY is missing or not set!\n"
        "Please add your Google API key to the .env file:\n"
        "   GOOGLE_API_KEY=your_actual_api_key_here\n\n"
        "Get your API key from: https://ai.google.dev/"
    )

# Initialize GenAI client
client = genai.Client(api_key=GOOGLE_API_KEY)


# ============================================================================
# MAIN FUNCTION - Use this in your application
# ============================================================================

def query_llm_with_image(query, image_path, model="gemini-2.5-flash"):
    """
    Sends a text query along with an image to Google GenAI and returns the model's response.
    
    Args:
        query (str): The text query/prompt to send to the model
        image_path (str): Path to the image file to analyze
        model (str): GenAI model to use (default: gemini-1.5-flash)
                    Available models: gemini-1.5-flash, gemini-1.5-pro, gemini-2.0-flash-exp
    
    Returns:
        str: The AI model's text response
        
    Raises:
        FileNotFoundError: If the image file doesn't exist
        Exception: If the API call fails
        
    Examples:
        >>> response = query_llm_with_image(
        ...     "What's wrong with this skin?",
        ...     "patient_skin.jpg"
        ... )
        >>> print(response)
        "Based on the image, you appear to have mild acne..."
    """
    # Validate image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ Image not found: {image_path}")
    
    # List of models to try (in order of preference)
    models_to_try = [model, "gemini-2.5-flash", "gemini-1.5-pro"]
    last_error = None
    
    for attempt_model in models_to_try:
        try:
            # Load image
            print(f"🖼️  Loading image: {image_path}")
            image = Image.open(image_path)
            
            # Send query + image to the AI model
            print(f"🤖 Querying {attempt_model}...")
            response = client.models.generate_content(
                model=attempt_model,
                contents=[query, image]
            )
            
            # Extract and return text response
            response_text = response.text
            print(f"✅ Response received ({len(response_text)} characters)")
            
            return response_text
            
        except Exception as e:
            error_msg = str(e)
            last_error = e
            
            # Check if it's a quota error
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
                print(f"⚠️  Quota exceeded for {attempt_model}, trying next model...")
                continue  # Try next model
            else:
                # For other errors, raise immediately
                print(f"❌ API Error with {attempt_model}: {e}")
                raise Exception(f"Failed to query LLM: {e}")
    
    # If all models failed
    print(f"❌ All models failed. Last error: {last_error}")
    raise Exception(
        f"Failed to query LLM with all models. Last error: {last_error}\n\n"
        f"💡 Suggestions:\n"
        f"1. Check your API quota at: https://ai.dev/usage\n"
        f"2. Wait a few minutes and try again\n"
        f"3. Consider upgrading your API plan at: https://ai.google.dev/pricing"
    )


# ============================================================================
# TESTING / EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🧠 BRAIN OF THE DOCTOR - TEST MODE")
    print("="*60 + "\n")
    
    # Test with a sample image (make sure this file exists!)
    test_image = "acne.jpg"
    test_query = (
        "You are a professional medical doctor. "
        "What do you see in this image? "
        "Is there any medical concern? "
        "Provide a brief, professional assessment."
    )
    
    if os.path.exists(test_image):
        try:
            result = query_llm_with_image(test_query, test_image)
            print(f"\n📋 AI Doctor's Response:\n")
            print(result)
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
    else:
        print(f"⚠️  Test image not found: {test_image}")
        print("   Please place a test image in the project directory to run the test.")
    
    print("\n" + "="*60)
    print("🏁 Test complete")
    print("="*60 + "\n")
