import random
from datetime import datetime

levels = ["INFO", "WARNING", "ERROR"]

normal_messages = [
    "User logged in",
    "Request processed",
    "File uploaded",
    "Database updated",
    "Payment successful",
    "Page loaded",
    "Cache cleared"
]

anomaly_messages = [
    "CRITICAL FAILURE ERROR ERROR",
    "System crash imminent",
    "Multiple payment failures detected",
    "Server overload detected",
    "Disk failure critical",
    "Unauthorized access attempt"
]

with open("app.log", "a") as f:
    for i in range(100):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if random.random() < 0.8:
            level = random.choice(["INFO", "WARNING"])
            message = random.choice(normal_messages)
        else:
            level = "ERROR"
            message = random.choice(anomaly_messages)

        log = f"{timestamp} | {level} | {message}\n"
        f.write(log)

print("100 logs generated in app.log")