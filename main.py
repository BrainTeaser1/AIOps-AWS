from mcp.server.fastmcp import FastMCP
from mcp.server.auth.settings import AuthSettings

from auth.cognito_verifier import CognitoTokenVerifier
from tools.alarms import get_active_alarms


mcp = FastMCP(
    "AWS Observability MCP",
    host="0.0.0.0",
    port=8000,

    auth=AuthSettings(
        issuer_url="https://cognito-idp.us-east-1.amazonaws.com/us-east-1_t8wytCttP",

        resource_server_url="https://appease-radiation-heat.ngrok-free.dev",

        required_scopes=[
            "default-m2m-resource-server-jfvkky/read"
        ]
    ),

    token_verifier=CognitoTokenVerifier()
)


@mcp.tool()
def list_cloudwatch_alarms():
    """
    Retrieve all CloudWatch alarms in the AWS account.

    Use this tool when:
    - The user asks about CloudWatch alarms
    - The user asks about monitoring status
    - The user asks about active alerts
    - The user asks about infrastructure health
    - The user asks about AWS observability

    Returns:
    - Alarm name
    - Alarm state
    """
    print("=" * 50)
    print("TOOL EXECUTED")
    print("=" * 50)

    return get_active_alarms()

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
