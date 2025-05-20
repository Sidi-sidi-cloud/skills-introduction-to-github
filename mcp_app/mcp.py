class Tool:
    """Base class for MCP tools."""

    def execute(self, instruction: str):
        raise NotImplementedError("Tool must implement execute")


class Orchestrator:
    """Simple MCP orchestrator that routes instructions to tools."""

    def __init__(self):
        self.tools = {}

    def register_tool(self, name: str, tool: Tool):
        self.tools[name] = tool

    def handle(self, instruction: str):
        """Parse instruction and dispatch to the correct tool."""
        # For simplicity, assume instruction starts with tool name
        parts = instruction.split(maxsplit=1)
        if not parts:
            return "No instruction provided"
        tool_name = parts[0].lower()
        payload = parts[1] if len(parts) > 1 else ""
        tool = self.tools.get(tool_name)
        if not tool:
            return f"Unknown tool: {tool_name}"
        return tool.execute(payload)
