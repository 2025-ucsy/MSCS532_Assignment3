from quicksort import randomized_quicksort
from hashtable import HashTable
from analysis import benchmark_sorting, hash_table_analysis

if __name__ == "__main__":
    print("Testing QuickSort:")
    arr = [9, 3, 5, 2, 7]
    print("Original array:", arr)
    print("Sorted array:", randomized_quicksort(arr))

    print("\nTesting HashTable:")
    ht = HashTable()
    ht.put("apple", 3)
    ht.put("banana", 5)
    print("Get apple:", ht.get("apple"))
    ht.remove("apple")
    print("Get apple after removal:", ht.get("apple"))

    benchmark_sorting()
    hash_table_analysis()
