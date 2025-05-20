from .mcp import Orchestrator


class ChatBot:
    """Simple chatbot using MCP orchestrator."""

    def __init__(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator

    def handle_message(self, message: str) -> str:
        return self.orchestrator.handle(message)
