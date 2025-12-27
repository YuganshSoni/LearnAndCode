from llm.base import LLMProvider
from langchain_openai import ChatOpenAI


class OpenaiProvider(LLMProvider):

    def __init__(self, config: dict):
        super().__init__(config)
        self.api_key = self.config["api_key"]
        self.model_name = self.config["model_name"]

    def create_llm(self)->ChatOpenAI:
        return ChatOpenAI(
            api_key=self.config['open_ai_api_key']
        ) 
