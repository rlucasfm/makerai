from llama_index.llms.openai import OpenAI
from motor.agents.Agent import Agent
from motor.prompttemplates.ConceptCreatorTemplates import concept_creator_template_base
from motor.tools import internet_search_tool

llm = OpenAI('gpt-4o-mini', max_retries=1)

class ConcepterAgent(Agent):
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(ConcepterAgent, cls).__new__(cls)
            cls.__instance.initialized = False
        return cls.__instance
    
    def __init__(self, tools=None, max_iterations=5, verbose=True):
        if not self.initialized:
            self.initialized = True
            super().__init__(llm, concept_creator_template_base, tools, max_iterations, verbose)