from typing import List, Dict, Any

class DataFilter:
    @staticmethod
    def filter_by_value(records: List[Dict[str, Any]], min_value: float) -> List[Dict[str, Any]]:
        return [
            r for r in records
            if float(r.get("value", 0)) >= min_value
        ]
