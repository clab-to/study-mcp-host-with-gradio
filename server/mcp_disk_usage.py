import json
import shutil
from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="mcp_disk_usage")


@mcp.tool()
async def get_disk_usage() -> str:
    """Get the disk usage"""
    total, used, free = shutil.disk_usage("/")
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)
    usage_percentage = (used / total) * 100
    disk_info = {
        "total_gb": round(total_gb, 2),
        "used_gb": round(used_gb, 2),
        "free_gb": round(free_gb, 2),
        "usage_percentage": round(usage_percentage, 2),
    }
    return json.dumps({
        "type": "text",
        "text": disk_info,
    })


if __name__ == "__main__":
    mcp.run(transport="stdio")
