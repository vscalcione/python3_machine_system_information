import psutil
import platform
from datetime import datetime
from .utils import get_size


print("="*40, "System Information", "="*40)

# System informations
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")

if uname.processor == "x86_64":
    print(f"Processor: {uname.processor} (64 bit)")
else:
    print(f"Processor: {uname.processor} (32 bit)")

# Boot time informations
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(
    f"Boot Time: {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")
