def heapify(arr, n, i):
    """
    Maintains the max-heap property for a subtree rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap Sort algorithm (in-place).
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)


# --------------------------
# User Input & Execution
# --------------------------
def main():
    try:
        size = int(input("Enter the number of elements in the array: "))
        if size <= 0:
            print("Size must be a positive integer.")
            return

        arr = []
        print(f"Enter {size} integers:")
        for _ in range(size):
            num = int(input())
            arr.append(num)

        print("\nOriginal array:")
        print(arr)

        heap_sort(arr)

        print("\nSorted array (ascending):")
        print(arr)

    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
