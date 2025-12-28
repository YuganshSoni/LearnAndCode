from llm.base import LLMProvider
from langchain_openai import ChatOpenAI

class OpenaiProvider(LLMProvider):
    def __init__(self, config: dict):
        super().__init__(config)

    def create_llm(self)->ChatOpenAI:
        return ChatOpenAI(
            **self.config
        )