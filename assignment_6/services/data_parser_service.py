from models.state_manager import StateManager
from logger.logger_service import LoggerService

class DataParser:
    @staticmethod
    def parse_data(state: StateManager, logger: LoggerService) -> None:
        logger.log("Parsing data...")
        parsed_records = []
        
        for line in state.raw_data:
            line_stripped = line.strip()
            if not line_stripped:
                continue

            parts = line_stripped.split(",")
            if len(parts) >= 3:
                record = {
                    "id": parts[0].strip(),
                    "name": parts[1].strip(),
                    "value": parts[2].strip()
                }
                if len(parts) >= 4:
                    record["date"] = parts[3].strip()
                parsed_records.append(record)
            else:
                error_msg = f"Invalid line format: {line}"
                state.add_error(error_msg)
                logger.log(f"ERROR: {error_msg}")
                
        state.parsed_records = parsed_records
        logger.log(f"Parsed {len(state.parsed_records)} records")