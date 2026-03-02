import re
def count_smileys(arr: list[str]) -> int:
    count = 0
    for text in arr:
        if re.search("[:;][-~]?[)D]", text):
            count += 1
    return count
