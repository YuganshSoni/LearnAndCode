from dotenv import load_dotenv
import os
load_dotenv()

current_provider_config = 'azure_openai_config'

openai_config = {
    "api_key" : os.getenv("OPENAI_API_KEY")
}

azure_openai_config = {
    "api_key" : os.getenv("AZURE_OPENAI_API_KEY"),
    "azure_endpoint" : os.getenv("AZURE_OPENAI_ENDPOINT"),
    "deployment_name" : os.getenv("DEPLOYMENT_NAME"),
    "api_version" : os.getenv("AZURE_API_VERSION")
}