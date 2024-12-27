from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool

## Internet search Tool
def internet_search(query: str):
    duckduckgo_spec = DuckDuckGoSearchToolSpec()
    return duckduckgo_spec.duckduckgo_full_search(query)

internet_search_tool = FunctionTool.from_defaults(
    fn=internet_search,
    name="Internet_search",
    description="this tool makes a search on the internet for any topic"
)