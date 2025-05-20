from ..mcp import Tool


class GmailTool(Tool):
    """Tool for sending emails via Gmail."""

    def __init__(self, credentials=None):
        self.credentials = credentials
        # TODO: initialize Gmail API client

    def execute(self, instruction: str):
        # In a real implementation, parse instruction to send an email
        return f"[Gmail] {instruction}"
