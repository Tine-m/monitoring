from prometheus_client import start_http_server, Counter, Gauge, Histogram
import psutil
import time
import random

# Define metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
CPU_LOAD = Gauge('cpu_load_percent', 'Current CPU Load Percentage')
REQUEST_DURATION = Histogram('request_duration_milliseconds', 'Request duration in milliseconds', buckets=(50, 100, 200, 300, 400, 500, 1000))

# Start up the server to expose metrics
start_http_server(8080)

# Function to simulate processing a request
def process_request():
    REQUESTS.inc()  # Increment the request counter
    
    # Simulate request duration
    duration = random.uniform(0.05, 1.0)  # Duration between 50ms and 1000ms
    time.sleep(duration)  # Simulate processing delay
    
    # Record the observed duration in milliseconds
    REQUEST_DURATION.observe(duration * 1000)  # Convert seconds to milliseconds

# Function to update CPU load percentage
def update_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1)  # Get CPU load percentage
    CPU_LOAD.set(cpu_load)  # Set the Gauge to the current CPU load

# Main loop
while True:
    process_request()  # Simulate handling a request
    update_cpu_load()  # Update the CPU load metric
