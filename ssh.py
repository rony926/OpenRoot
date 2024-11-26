import subprocess
import re

def get_localhost_run_url(port=9000):
    try:
        # Command to start the SSH tunnel
        # command = [
        #     "ssh", "-R", f"80:localhost:{port}", "ssh.localhost.run"
        # ]
        command = [
            "ssh", "-R", f"80:localhost:{port}", "ssh.serveo.net"
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
        return "No URL found. Ensure localhost.run/serveo.net is accessible."
    
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = get_localhost_run_url(port=9000)
    print(f"Your public URL is: {url} \n")

