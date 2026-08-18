import argparse
import socket
import time
import threading

open_ports = []
lock = threading.Lock() 

parser = argparse.ArgumentParser()
parser.add_argument("--ip", help="Target IP")
parser.add_argument("--start", type=int, help="First port")
parser.add_argument("--end", type=int, help="Last port")
args = parser.parse_args()

open_fayl = f"OPEN_{args.ip}.txt"

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  
        netice = s.connect_ex((ip, port))
        s.close()
        
        if netice == 0:
            with lock:
                open_ports.append(port)
    except Exception:
        pass
    
start_zaman = time.perf_counter()
threads = []

for i in range(args.start, args.end + 1):
    t = threading.Thread(target=scan_port, args=(args.ip, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

finish_zaman = time.perf_counter()
print(f"The scan took {finish_zaman - start_zaman:.4f} seconds")

if open_ports:
    sorted_open = sorted(open_ports)
    print(f"Open ports: {sorted_open}")
    with open(open_fayl, "w") as f:
        for p in sorted_open:
            f.write(f"Port-{p} is open\n")
    print(f"Results saved to {open_fayl}")
else:
    print("No open ports were found.")