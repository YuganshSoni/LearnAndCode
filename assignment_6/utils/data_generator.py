import random
from datetime import datetime, timedelta

class DataGenerator:
    @staticmethod
    def generate_sample_data(file_path: str, record_count: int):
        with open(file_path, "w") as f:
            for i in range(1, record_count + 1):
                record_id = f"ID{i:04d}"
                name = f"Item{i}"
                value = random.randint(10, 1000)
                date = datetime.now() - timedelta(days=random.randint(0, 365))
                f.write(f"{record_id},{name},{value},{date:%Y-%m-%d}\n")
        print(f"Generated {record_count} sample records in {file_path}")
