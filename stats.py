import string
from typing import Dict, List, Any

def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_counts(text: str) -> int:
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def create_char_count_records(dct: Dict[str, int]) -> List[Dict[str, Any]]:
    records = [{"char": char, "num": count} for char, count in dct.items()]
    records.sort(key=lambda x: x["num"], reverse=True)
    return records

