from mcp.server.fastmcp import FastMCP
from app import get_crypto_price

mcp = FastMCP("weather-forecast-mcp")

@mcp.tool()
async def get_crypto_price(coin_id: str) -> dict:
    result = get_crypto_price(coin_id)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")