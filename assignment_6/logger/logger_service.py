from datetime import datetime
from typing import List

class LoggerService:
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self.log_buffer: List[str] = []

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_buffer.append(f"[{timestamp}] {message}")

    def save_logs(self):
        with open(self.log_file_path, "w") as f:
            f.write("\n".join(self.log_buffer))
