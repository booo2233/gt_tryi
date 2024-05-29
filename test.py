"""
from PIL import Image
import os
from settings import *
import google.generativeai as genai
from dotenv import load_dotenv
import asyncio
load_dotenv()

key : str = os.getenv("GEMINI_API_KEY")

async def handle_response_image(text: str) -> str:
 genai.configure(api_key=key)


# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
 generation_config : dict = generation_configes
 safety_settings : list = safety_settingses


 model = genai.GenerativeModel(
   model_name = "gemini-1.5-pro",
   safety_settings = safety_settings,
   generation_config = generation_config,
 )

 img = Image.open('E:\\Python\\discon\\discord_tutorial_2024-main\\discord_tutorial_2024-main\\bot\\image.jpg')
 img

 response = model.generate_content([text, img], stream=True)
 response.resolve()
 
 return response.text

print(handle_response_image("what is in image"))
"""
import yt_dlp

print(dir(yt_dlp))