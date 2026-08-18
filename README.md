# Multithreaded TCP Port Scanner

A fast and efficient command-line TCP port scanner built in Python. It utilizes multithreading (`threading` module) and socket programming to scan a range of ports concurrently, significantly reducing execution time compared to sequential scanning.

## Features
- **Multithreading:** Scans multiple ports simultaneously for high performance.
- **Customizable Range:** Define target IP address, start port, and end port using command-line arguments.
- **Timeout Control:** Implements socket timeout to prevent hanging on closed or filtered ports.
- **File Export:** Automatically saves open ports to a text file (`OPEN_[IP].txt`).
- **Thread Safety:** Uses `threading.Lock()` to prevent race conditions when appending results to shared lists.

## Prerequisites
- Python 3.x

## Usage
Run the script from your terminal by specifying the target IP, start port, and end port:

```bash
python port_scanner_threaded.py --ip 127.0.0.1 --start 1 --end 20000

## Example Output

```text
The scan took 9.7140 seconds
Open ports: [135, 445, 902, 912, 4709, 5040]
Results saved to OPEN_127.0.0.1.txt