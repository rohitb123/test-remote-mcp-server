
from fastmcp import FastMCP
import random

# Initialize the MCP server with a name
mcp = FastMCP("Simple Calculator Server")

# Tool 1: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

# Tool 2: Generate random number
@mcp.tool()
def random_number(min_val: int, max_val: int) -> int:
    """
    Generate a random number within a given range.
    
    Args:
        min_val: Minimum value
        max_val: Maximum value
    
    Returns:
        Random number between min_val and max_val
    """
    return random.randint(min_val, max_val)

# Resource : Server information
@mcp.resource("server:///info", mime_type="application/json")
def server_info():
    """
    Get information about this MCP server.
    
    Returns:
        Dictionary with server information
    """
    return {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic remote MCP server for testing"
    }

# Start the server
if __name__ == "__main__":
    # KEY CHANGE : Use HTTP transport for remote access
    mcp.run(transport="http", host="0.0.0.0", port=8000)
