from langchain_core.prompts import PromptTemplate

class Prompt:
    def get_prompt_template():
        prompt_template = PromptTemplate(
                template="""
                    you are an marketing agent,  you can provide assistance to users for marketing queries only.
                    you MUST stick to marketing related queries only.
                    user query : {user_query}
                """, input_variables=["user_query"]
            )
        return prompt_template