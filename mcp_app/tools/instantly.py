from ..mcp import Tool


class InstantlyTool(Tool):
    """Tool for triggering Instantly.ai outreach campaigns."""

    def __init__(self, api_key=None):
        self.api_key = api_key
        # TODO: store API key and prepare HTTP client

    def execute(self, instruction: str):
        # In a real implementation, call Instantly.ai API
        return f"[Instantly] {instruction}"
