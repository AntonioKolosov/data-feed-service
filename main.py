"""
For development purpose only
"""

import os
import sys

from pyngrok import ngrok
import uvicorn


if __name__ == "__main__":
    PORT = 8003
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    HOST = "127.0.0.1"
    # Create tunnels for 
    # http
    http_tunnel = ngrok.connect(PORT, bind_tls=True)
    external_https = http_tunnel.public_url
    os.environ['EXTERNAL_HTTPS'] = external_https
    # tcp (wss)
    # tcp_tunnel = ngrok.connect(PORT, "tcp")
    # external_tcp = tcp_tunnel.public_url
    # os.environ['EXTERNAL_TCP'] = external_tcp

    # Run the server
    uvicorn.run("src.app:app", port=PORT, host=HOST,
                log_level="info", reload=True)

    # Close the tunnels
    print("disconnect and kill the tunnels")
    ngrok.disconnect(external_https)
    # ngrok.disconnect(external_tcp)
    ngrok.kill()