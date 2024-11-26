import random

# Generate 50 random integers between 0 and 100 with seed 40
random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

sorted_data = merge_sort(data)

# Print original and sorted data
print("Original Data:", data)
print("Sorted Data (Merge Sort):", sorted_data)
