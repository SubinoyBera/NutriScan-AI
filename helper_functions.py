# Helper functions for image processing and LLM interaction
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))     #type: ignore


class HelperFunctions:
    def __init__(self) -> None:
        """
        Constructor for the HelperFunctions class
        """
        pass

    def prepare_image_data(self, image):
        """
        Prepare image data for submission to LLM.

        If an image is provided, reads the bytes data from the image file and 
        constructs a list of dictionaries containing the mime type and image data.

        Args:
            image (File): The image file to be processed

        Returns:
            List[Dict[str, Union[str, bytes]]]: A list of dictionaries containing
            the mime type and image data

        Raises:
            FileNotFoundError: If no file is provided
        """
        if image is not None:
            bytes_data = image.getvalue()
            img_parts = [
                {
                    "mime_type": image.type,
                    "data": bytes_data 
                }
            ]
            return img_parts
        else:
            raise FileNotFoundError("No file uploaded. Please upload an image.")


    def analyze_food_image(self, prompt, image_data):
        """
        Analyze the provided food image using a Gen AI Large Language Model (LLM)
        and return a text summary of the analysis.

        Args:
            prompt (str): The prompt to be passed to the LLM
            image_data (List[Dict[str, Union[str, bytes]]]): A list of dictionaries containing
            the mime type and image data

        Returns:
            str: The text summary of the analysis
        """
        llm = genai.GenerativeModel("gemini-2.5-pro")                       #type: ignore
        response = llm.generate_content([prompt, image_data[0]])

        return response.text