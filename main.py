# TASK1
def selection_sort(numbers: list):
    n = len(numbers)
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i):
            if numbers[j] > numbers[max_index]:
                max_index = j
        if max_index != i:
            numbers[i], numbers[max_index] = numbers[max_index], numbers[i]


# TASK2
def binary_search(text: list, target: str):
    low = 0
    high = len(text) - 1
    while low <= high:
        mid = (low + high) // 2
        if text[mid] == target:
            return text[mid]
        elif text[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


class HashTable:
    def __init__(self, size):  # TASK3
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):  # TASK4
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return len(key) % self.size
        else:
            raise TypeError("Key must be an integer or a string.")

    def put(self, key, data):  # TASK5
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):  # TASK6
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None
