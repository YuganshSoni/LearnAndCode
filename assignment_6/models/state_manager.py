from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class StateManager:
    input_file_path: str
    output_file_path: str
    log_file_path: str = "processing.log"

    records_processed: int = 0
    error_count: int = 0
    error_messages: List[str] = field(default_factory=list)

    validate_data: bool = True
    transform_data: bool = True
    date_format: str = "%Y-%m-%d"
    batch_size: int = 100

    statistics: Dict[str, Any] = field(default_factory=dict)
    
    raw_data: List[str] = field(default_factory=list)
    parsed_records: List[Dict[str, Any]] = field(default_factory=list)

    def add_error(self, message: str):
        self.error_count += 1
        self.error_messages.append(message)
