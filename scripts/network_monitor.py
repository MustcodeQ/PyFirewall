import os

def start_tcpdump():
    """Start network traffic monitoring using tcpdump."""
    print("Starting tcpdump to capture network traffic...")
    try:
        os.system("sudo tcpdump -i any -n")
    except KeyboardInterrupt:
        print("\nStopped tcpdump.")

if __name__ == "__main__":
    start_tcpdump()
