"""
For development purpose only
"""

import os
import sys

import uvicorn


if __name__ == "__main__":
    PORT = 8003
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    HOST = "127.0.0.1"

    # Run the server
    uvicorn.run("src.app:app", port=PORT, host=HOST,
                log_level="info", reload=True)
