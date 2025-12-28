from llm.providers.azure_openai_provider import AzureOpenaiProvider
from llm.providers.openai_provider import OpenaiProvider
from config import openai_config, azure_openai_config, current_provider_config

def get_model():
    if current_provider_config=="openai_config":
        openai = OpenaiProvider(openai_config)
        return openai.create_llm()
    else:
        azure_openai = AzureOpenaiProvider(azure_openai_config)
        return azure_openai.create_llm()