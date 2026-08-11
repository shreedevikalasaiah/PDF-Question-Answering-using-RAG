from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME


class LLM:

    @staticmethod
    def load():

        if not GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is missing. Add it to a .env file in the project root."
            )

        return ChatGroq(
            model=MODEL_NAME,
            api_key=GROQ_API_KEY,
            temperature=0
        )