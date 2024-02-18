import http.server
import socketserver

# Set the port number you want to use
port = 3433

# Specify the directory containing your HTML files
directory = "/home/user/web/ex2/"  # You can change this to the directory you want to serve

# Create a simple handler to serve the files
handler = http.server.SimpleHTTPRequestHandler

# Set up the server
httpd = socketserver.TCPServer(("", port), handler)

# Print a message indicating the server is running
print(f"Serving on port {port}. Open http://localhost:{port} in your web browser.")

# Start the server
httpd.serve_forever()