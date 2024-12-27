from llama_index.core import VectorStoreIndex
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.chat_engine import SimpleChatEngine

class Agent:
    def __init__(self, llm, context, tools=None, max_iterations=5, verbose=True):
        self.llm = llm
        self.context = context
        self.tools = tools,
        self.max_iterations = max_iterations,
        self.verbose = verbose

        if tools is None:
            self.agent = SimpleChatEngine.from_defaults(
                llm=llm,
                system_prompt=context,
                verbose=verbose
            )
        else:
            self.agent = ReActAgent.from_tools(
                tools=tools,
                llm=llm,
                max_iterations=max_iterations,
                context=context,
                verbose=verbose,
                chat_history=[
                    ChatMessage(
                        role="system",
                        content="USE TOOLS IF NEEDED."
                    )
                ]
            )

