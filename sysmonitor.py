import psutil
import logging
import time
from datetime import datetime

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Define thresholds
CPU_THRESHOLD = 80.0  # percent
MEMORY_THRESHOLD = 80.0  # percent
DISK_THRESHOLD = 80.0  # percent

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {usage}%')
    return usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {usage}% used')
    return usage

def check_running_processes():
    processes = len(psutil.pids())
    logging.info(f'Number of running processes: {processes}')
    return processes

def monitor_system():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        processes = check_running_processes()

        print(f"\rCPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}% | Running Processes: {processes}", end="")
        
        time.sleep(3)

if __name__ == "__main__":
    monitor_system()
