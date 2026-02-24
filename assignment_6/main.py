from models.state_manager import StateManager
from services.data_processor_service import DataProcessor
from services.file_handler_service import FileHandlerService
from utils.data_generator import DataGenerator
from utils.data_filter import DataFilter

if __name__ == "__main__":
    DataGenerator.generate_sample_data("input.csv", 50)

    state = StateManager(
        input_file_path="input.csv",
        output_file_path="output.csv",
        date_format="%m/%d/%Y",
        batch_size=50
    )

    processor_service = DataProcessor(state)
    processor_service.process_data()
    processor_service.display_statistics()

    FileHandlerService.export_to_json("output.json", state.parsed_records)
    FileHandlerService.export_to_xml("output.xml", state.parsed_records)

    try:
        FileHandlerService.export_by_format("output_test.json", state.parsed_records, "json")
    except Exception as ex:
        print(f"Export error: {ex}")

    filtered = DataFilter.filter_by_value(state.parsed_records, 100)
    print(f"\nFiltered records: {len(filtered)}")

    print(f"\nRecords processed: {state.records_processed}")
    print(f"Errors: {state.error_count}")

    state.error_messages.append("Manually added error")