from datetime import datetime
from models.state_manager import StateManager
from logger.logger_service import LoggerService

class DataTransformer:
    @staticmethod
    def transform_data(state: StateManager, logger: LoggerService) -> None:
        logger.log("Transforming data...")
        for record in state.parsed_records:
            if "name" in record:
                record["name"] = record["name"].upper()

            if "date" in record:
                try:
                    date_obj = datetime.strptime(record["date"], "%Y-%m-%d")
                    record["date"] = date_obj.strftime(state.date_format)
                except ValueError:
                    pass

            if "value" in record:
                try:
                    value = float(record["value"])
                    record["doubled_value"] = value * 2
                    record["squared_value"] = value ** 2
                except ValueError:
                    pass
        logger.log("Transformation complete")
