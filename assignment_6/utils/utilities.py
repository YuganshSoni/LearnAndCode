from datetime import datetime

def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_buffer.append(f"[{timestamp}] {message}")

def display_statistics(self):
    print("\n=== Processing Statistics ===")
    for key, value in self.statistics.items():
        print(f"{key}: {value}")

    if self.error_messages:
        print("\n=== Errors ===")
        for error in self.error_messages:
            print(f"- {error}")