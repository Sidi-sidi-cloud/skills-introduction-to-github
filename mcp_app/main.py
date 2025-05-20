"""Command line entry point for the MCP chatbot demo."""

from .mcp import Orchestrator
from .chatbot import ChatBot
from .tools.google_sheets import GoogleSheetsTool
from .tools.gmail import GmailTool
from .tools.instantly import InstantlyTool


def setup_orchestrator() -> Orchestrator:
    orchestrator = Orchestrator()
    orchestrator.register_tool("sheets", GoogleSheetsTool())
    orchestrator.register_tool("gmail", GmailTool())
    orchestrator.register_tool("instantly", InstantlyTool())
    return orchestrator


def main():
    orchestrator = setup_orchestrator()
    bot = ChatBot(orchestrator)

    print("Type instructions prefixed with tool name (e.g. 'gmail send to foo')")
    try:
        while True:
            msg = input("You: ")
            if msg.lower() in {"exit", "quit"}:
                break
            reply = bot.handle_message(msg)
            print("Bot:", reply)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
