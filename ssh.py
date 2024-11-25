# import subprocess

# # Function to run the serveo.net SSH command
# def get_serveo_url():
#     # Run the SSH command for reverse tunneling
#     # The `-R` flag means "remote forwarding" to bind to a port on the remote server (serveo.net).
#     # Replace `8000` with the port number of your local application.
#     command = ["ssh", "-R", "80:localhost:8000", "serveo.net"]
    
#     # Run the command in the background and capture the output
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Capture the output
#     stdout, stderr = process.communicate()

#     # If there was an error, print it
#     if stderr:
#         print(f"Error: {stderr.decode()}")
    
#     # Otherwise, look for the URL in the output
#     for line in stdout.decode().splitlines():
#         if "https://" in line:
#             print(f"Your Serveo URL is: {line.strip()}")
#             return line.strip()

#     # If no URL is found, return a message
#     return "No URL found in the response."

# # Call the function to get the Serveo URL
# get_serveo_url()

import subprocess
import re

def get_localhost_run_url(port=9000):
    try:
        # Command to start the SSH tunnel
        command = [
            "ssh", "-R", f"80:localhost:{port}", "ssh.localhost.run"
        ]
        
        # Start the subprocess
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Read the output for the URL
        for line in process.stdout:
            print(line, end="")  # Optional: Print the output
            match = re.search(r"https?://[^\s]+", line)
            if match:
                inf = match.group(0)
                f = open("myip.txt", "w")
                f.write(inf)
                f.close()
                return inf
        
        # If no URL is found, return an error
        return "No URL found. Ensure localhost.run is accessible."
    
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = get_localhost_run_url(port=9000)
    print(f"Your public URL is: {url}")

