from abc import ABC, abstractmethod
from langchain_core.runnables import Runnable

class LLMProvider(ABC):
    """Base class for defining contract of all llm provider"""

    def __init__(self, config : dict):
        self.config = config
        self._llm = None
    
    #forces base class to implement create_llm method(run time polymorphism[method overriding])
    @abstractmethod
    def create_llm(self)->Runnable:
        pass