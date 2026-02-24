import json
import os
from typing import List, Dict, Any

class FileHandlerService:
    
    @staticmethod
    def ensure_file_exists(file_path: str):
        if not os.path.exists(file_path):
            open(file_path, "w").close()

    @staticmethod
    def read_file(file_path: str) -> List[str]:
        with open(file_path, "r") as f:
            return f.read().splitlines()

    @staticmethod
    def write_csv(file_path: str, records: List[Dict[str, Any]]):
        with open(file_path, "w") as f:
            f.write("ID,NAME,VALUE,DATE,DOUBLED_VALUE,SQUARED_VALUE\n")
            for record in records:
                line = (
                    f"{record.get('id', '')},{record.get('name', '')},{record.get('value', '')},"
                    f"{record.get('date', '')},{record.get('doubled_value', '')},{record.get('squared_value', '')}\n"
                )
                f.write(line)

    @staticmethod
    def export_to_json(file_path: str, records: List[Dict[str, Any]]):
        with open(file_path, "w") as f:
            json.dump(records, f, indent=2)

    @staticmethod
    def export_to_xml(file_path: str, records: List[Dict[str, Any]]):
        with open(file_path, "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<records>\n')
            for record in records:
                f.write("  <record>\n")
                for k, v in record.items():
                    f.write(f"    <{k}>{v}</{k}>\n")
                f.write("  </record>\n")
            f.write("</records>")

    @classmethod
    def export_by_format(cls, file_path: str, records: List[Dict[str, Any]], format_type: str):
        format_type = format_type.lower()
        if format_type == "json":
            cls.export_to_json(file_path, records)
        elif format_type == "xml":
            cls.export_to_xml(file_path, records)
        elif format_type == "csv":
            with open(file_path, "w") as f:
                f.write("ID,NAME,VALUE\n")
        else:
            raise ValueError(f"Unsupported format: {format_type}")
