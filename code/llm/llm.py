import os

from google import genai

from llm.model import LLMResponse
from log import get_logger

logger = get_logger(__name__)

class LLM:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)


    def generate_content(self, running_data: dict) -> LLMResponse | None:
        try:
            prompt = f"""
            This is data of the latest run recorded on Strava. Please analyse the given data and provide a summary of the run and how the user can improve. 
            Please format the output to the user in the following way:
            **Summary of the Run**

            **Analysis and Potential Areas for Improvement:**

            **Overall Recommendations:**

            {running_data}
            """
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            logger.info(f"AI Response -> {response.text}")
            return LLMResponse.from_str(data=str(response.text))
        except (Exception) as e:
            logger.error(f"Error: {e}")
            raise ValueError(f"Error {e}")
