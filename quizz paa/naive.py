import random

# Generate 50 random integers between 0 and 100 with seed 40
random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_data = bubble_sort(data)

# Print original and sorted data
print("Original Data:", data)
print("Sorted Data (Bubble Sort):", sorted_data)
