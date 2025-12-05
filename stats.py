from typing import Dict, List

def get_num_words(text: str) -> int:
    count = len(text.split())
    print(f"Found {count} total words")

def get_char_counts(text: str) -> Dict[str, int]:
    char_counts = {}
    _text = text.replace("\ufeff", "")
    for c in _text:
        lc = c.lower()
        if not lc in char_counts:
            char_counts[lc] = 1
            continue
        char_counts[lc] += 1
    return char_counts

def sort_by_count(counts):
    return counts["num"]

def sort_char_counts(cc: Dict[str, int]) -> List:
    result = []
    for k, v in cc.items():
        result.append({ "char": k, "num": v})
    result.sort(reverse=True, key=sort_by_count)
    return result