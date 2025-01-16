# Firewall Project

## Project Overview
This project simulates a simple firewall using Python scripts. It reads firewall rules from a JSON file and logs the status of connections (allowed or blocked). It also includes a network monitoring script using `tcpdump`.

## File Structure
- `config/firewall_rules.json`: Configuration file for firewall rules.
- `logs/firewall_log.txt`: Log file for recording allowed and blocked connections .
- `scripts/config_loader.py`: Helper script to load firewall configuration.
- `scripts/firewall_simulator.py`: Main script for simulating firewall behavior.
- `scripts/network_monitor.py`: Script for capturing network traffic using `tcpdump`.
- `README.md`: Project documentation.

## Installation and Setup
1. Ensure Python 3 is installed.
2. Install `tcpdump`:
   ```bash
   sudo apt update
   sudo apt install tcpdump
   ```
3. Install Python dependencies (if any):
   ```bash
   pip install -r requirements.txt  # If you have a requirements file.
   ```

## Usage

### Running the Firewall Simulator
1. Run the simulator:
   ```bash
   python3 scripts/firewall_simulator.py
   ```
2. Check the `logs/firewall_log.txt` file for the connection logs.

### Running the Network Monitor
1. Run the monitor:
   ```bash
   sudo python3 scripts/network_monitor.py
   ```
2. Observe real-time network traffic.

## Configuration
Edit `config/firewall_rules.json` to modify the firewall rules:

```json
{
  "blocked_ips": ["192.168.1.1", "192.168.1.3"],
  "allowed_ips": ["192.168.1.2"],
  "blocked_ports": [80, 443]
}
```

## License
This project is licensed under the MIT License.

---

### Next Steps
- Test the `firewall_simulator.py` script by simulating different connections and verifying that logs are updated in `firewall_log.txt`.
- Use `network_monitor.py` to capture and display network traffic to ensure your firewall rules are effective.
