from typing import List, Dict, Any

from models.state_manager import StateManager
from services.file_handler_service import FileHandlerService
from services.data_parser_service import DataParser
from services.data_validator_service import DataValidator
from services.data_transformer_service import DataTransformer
from services.statistics_service import StatisticsService
from logger.logger_service import LoggerService

class DataProcessor:
    def __init__(self, state: StateManager):
        self.state = state
        self.logger = LoggerService(self.state.log_file_path)

        FileHandlerService.ensure_file_exists(self.state.input_file_path)
        self.logger.log("DataProcessor initialized with StateManager")

    def process_data(self):
        self.logger.log("Starting data processing")

        try:
            self.logger.log(f"Reading input file: {self.state.input_file_path}")
            self.state.raw_data = FileHandlerService.read_file(self.state.input_file_path)
            self.logger.log(f"Read {len(self.state.raw_data)} lines")

            DataParser.parse_data(self.state, self.logger)

            if self.state.validate_data:
                DataValidator.validate_data(self.state, self.logger)

            if self.state.transform_data:
                DataTransformer.transform_data(self.state, self.logger)

            StatisticsService.calculate_statistics(self.state, self.logger)

            self.logger.log(f"Writing output to: {self.state.output_file_path}")
            FileHandlerService.write_csv(self.state.output_file_path, self.state.parsed_records)
            
            self.state.records_processed = len(self.state.parsed_records)
            self.logger.log(f"Output written. {self.state.records_processed} records processed")

            self.logger.save_logs()

            print("Processing complete!")
            print(f"Records processed: {self.state.records_processed}")
            print(f"Errors: {self.state.error_count}")

        except Exception as ex:
            self.state.add_error(f"Fatal error: {ex}")
            self.logger.log(f"FATAL ERROR: {ex}")
            print(f"Processing failed: {ex}")

    def display_statistics(self):
        print("\n=== Processing Statistics ===")
        for k, v in self.state.statistics.items():
            print(f"{k}: {v}")

        if self.state.error_messages:
            print("\n=== Errors ===")
            for e in self.state.error_messages:
                print(f"- {e}")
