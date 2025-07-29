# Heap-based approach
# Time Complexity:
# O(N log K) → Building frequency map (O(N)) + maintaining heap (O(log K) per item).

# Space Complexity:
# O(N) for the frequency map
# O(K) for the heap

# Count Frequencies: Use a hash map (seen) to count how often each number appears in nums.
# Use Min-Heap: Maintain a min-heap (arr) of size k to keep the top k most frequent elements.
# Heap Trim: If the heap exceeds size k, remove the least frequent element.
# Extract Results: Return the elements (not their frequencies) from the heap.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}  # Dictionary 

        # Count frequency of each number
        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        arr = []  # an array for Min-heap to keep top k frequent elements 

        # Build a heap of (frequency, number) pairs
        for num, freq in seen.items():
            heapq.heappush(arr, (freq, num))  # Push current (freq, num) into the heap
            if len(arr) > k:
                heapq.heappop(arr)  # Remove least frequent element if heap exceeds size k

        # Extract only the number (second element) from each (freq, num) tuple
        return [n for i, n in arr]
# //=================================================================================================
