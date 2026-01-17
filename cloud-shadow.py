import requests
import argparse
import concurrent.futures
import random
import urllib3

# Cloud-Shadow: Infrastructure & Metadata Leakage Hunter
# Author: @canmitm | ahmetcan0x01@gmail.com
# Use only for authorized security auditing.

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CloudShadow:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.agents = [
            "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
        ]

    def get_headers(self):
        return {
            "User-Agent": random.choice(self.agents),
            "Metadata-Flavor": "Google",
            "X-Forwarded-For": "127.0.0.1",
            "X-Originating-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "X-Client-IP": "127.0.0.1"
        }

    def audit(self, path):
        url = f"{self.target}/{path.lstrip('/')}"
        try:
            r = requests.get(url, headers=self.get_headers(), timeout=6, verify=False, allow_redirects=False)
            if r.status_code in [200, 204, 301, 302, 307, 401, 403, 405, 500]:
                print(f"[!] {r.status_code} | Size: {len(r.text)} | Path: /{path}")
        except:
            pass

    def start_engine(self, workers):
        with open('shadow_payloads.lst', 'r') as f:
            paths = [line.strip() for line in f if line.strip()]

        print(f"[*] Target: {self.target}")
        print(f"[*] Payload Count: {len(paths)}")
        print(f"[*] Thread Count: {workers}")
        print("-" * 60)

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            executor.map(self.audit, paths)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cloud-Shadow Recon")
    parser.add_argument("-t", "--target", required=True, help="Target URL")
    parser.add_argument("-w", "--workers", type=int, default=15, help="Threads (default 15)")
    args = parser.parse_args()

    hunter = CloudShadow(args.target)
    hunter.start_engine(args.workers)
