from models.state_manager import StateManager
from logger.logger_service import LoggerService

class DataValidator:
    @staticmethod
    def validate_data(state: StateManager, logger: LoggerService) -> None:
        logger.log("Validating data...")
        valid_records = []

        for record in state.parsed_records:
            is_valid = True

            if not record.get("id"):
                is_valid = False
                state.add_error("Record missing ID")

            if not record.get("name"):
                is_valid = False
                state.add_error(f"Record {record.get('id')} missing name")

            if "value" in record:
                try:
                    float(record["value"])
                except ValueError:
                    is_valid = False
                    state.add_error(f"Record {record.get('id')} has invalid value")

            if is_valid:
                valid_records.append(record)

        state.parsed_records = valid_records
        logger.log(f"Validation complete. {len(state.parsed_records)} valid records")