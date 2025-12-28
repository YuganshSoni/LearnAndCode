from llm.base import LLMProvider
from langchain_openai import AzureChatOpenAI
class AzureOpenaiProvider(LLMProvider):
    def __init__(self, config: dict):
        super().__init__(config)

    def create_llm(self)->AzureChatOpenAI:
        return AzureChatOpenAI(
            **self.config 
        )