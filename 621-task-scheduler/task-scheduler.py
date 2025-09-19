from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_freq)

        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count

        return max(len(tasks), empty_slots)
