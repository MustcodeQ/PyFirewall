from config_loader import load_config

# Load configuration
config = load_config('../config/firewall_rules.json')

def check_connection(ip, port):
    """Check if the given IP and port should be allowed or blocked."""
    if not config:
        print("No firewall configuration loaded.")
        return False
    
    # Check if the IP is in the blocked list
    if ip in config.get('blocked_ips', []):
        return False  # Blocked by IP
    
    # Check if the IP is in the allowed list
    if ip in config.get('allowed_ips', []):
        return True  # Allowed by IP
    
    # Check if the port is in the blocked ports list
    if port in config.get('blocked_ports', []):
        return False  # Blocked by port

    # Default rule: allow if not explicitly blocked
    return True

def log_connection(ip, port, status):
    """Log the connection status to a file."""
    with open("../logs/firewall_log.txt", "a") as log_file:
        log_file.write(f"{ip} on port {port} - {'Allowed' if status else 'Blocked'}\n")

def main():
    # Simulate a list of incoming connections (IP, Port)
    connections = [("192.168.1.1", 80), ("192.168.1.2", 22), ("10.0.0.1", 443), ("192.168.1.3", 8080)]
    
    for ip, port in connections:
        status = check_connection(ip, port)
        if status:
            print(f"Connection from {ip} on port {port} is allowed.")
        else:
            print(f"Connection from {ip} on port {port} is blocked.")
        
        log_connection(ip, port, status)

if __name__ == "__main__":
    main()
