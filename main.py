from mcp.server.fastmcp import FastMCP

from tools.alarms import get_active_alarms

mcp = FastMCP(
    "AWS Observability MCP",
    host="0.0.0.0",
    port=8000
)

@mcp.tool()
def list_cloudwatch_alarms():
    """
    List all CloudWatch alarms and their current states.
    """
    return get_active_alarms()

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
