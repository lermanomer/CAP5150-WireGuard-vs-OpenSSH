import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

if len(sys.argv) < 2:
    print("Usage: python3 http_scalability_test.py <URL1> [URL2 URL3 ...]")
    sys.exit(1)

urls = sys.argv[1:]

TOTAL_REQUESTS = 100
WORKERS = 10

requests = []

for i in range(TOTAL_REQUESTS):
    requests.append(urls[i % len(urls)])

def make_request(url):
    with urllib.request.urlopen(url, timeout=10) as response:
        response.read()
        return response.status

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=WORKERS) as executor:
    futures = [executor.submit(make_request, url) for url in requests]

    successful = 0

    for future in as_completed(futures):
        try:
            if future.result() == 200:
                successful += 1
        except Exception:
            pass

end = time.perf_counter()

elapsed = end - start
requests_per_second = TOTAL_REQUESTS / elapsed

print(f"Services tested: {len(urls)}")
print(f"Total requests: {TOTAL_REQUESTS}")
print(f"Concurrent workers: {WORKERS}")
print(f"Successful requests: {successful}")
print(f"Completion time: {elapsed:.4f} seconds")
print(f"Requests per second: {requests_per_second:.2f}")
