import time
import random
from quicksort import randomized_quicksort
from hashtable import HashTable

def benchmark_sorting():
    print("QuickSort Benchmark:")
    for size in [1000, 5000, 10000]:
        arr = [random.randint(0, 100000) for _ in range(size)]
        start = time.time()
        randomized_quicksort(arr)
        end = time.time()
        print(f"Size: {size}, Time: {end - start:.4f} seconds")

def hash_table_analysis():
    print("\nHash Table Load Factor Analysis:")
    for size in [10, 100, 1000]:
        ht = HashTable(capacity=size)
        collisions = 0
        inserted_keys = set()
        for i in range(size * 2):
            key = f"key{i}"
            if key in inserted_keys:
                continue
            inserted_keys.add(key)
            index = ht._hash(key)
            if ht.table[index]:
                collisions += 1
            ht.put(key, i)
        print(f"Capacity: {size}, Items: {size*2}, Collisions: {collisions}")
