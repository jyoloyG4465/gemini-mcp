from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("dajyare")


@mcp.tool()
def get_dajyare() -> str:
    return "布団がふっとんだ"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
