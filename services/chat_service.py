from prompts.prompt import Prompt
from utils.model import get_model

class ChatService:
    def create_chain(self, prompt, model):
        return prompt | model
        
    def chat_response(self, user_query: str):
        prompt_template = Prompt.get_prompt_template()
        llm_model = get_model()
        chain = self.create_chain(prompt_template, llm_model)
        result = chain.invoke({'user_query' : user_query})
        return result.content