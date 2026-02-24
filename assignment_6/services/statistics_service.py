from models.state_manager import StateManager
from logger.logger_service import LoggerService

class StatisticsService:
    @staticmethod
    def calculate_statistics(state: StateManager, logger: LoggerService) -> None:
        logger.log("Calculating statistics...")
        
        total_value = sum(float(r["value"]) for r in state.parsed_records if "value" in r)

        state.statistics["total_records"] = len(state.parsed_records)
        state.statistics["error_count"] = state.error_count
        state.statistics["total_value"] = int(total_value)
        
        state.statistics["average_value"] = (
            int(total_value / len(state.parsed_records)) if state.parsed_records else 0
        )
        
        logger.log(f"Statistics calculated: {len(state.statistics)} metrics")
