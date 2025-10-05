# Sorting Visualizer Project
# Author: Sri Harsha
# Date: March 2025
# Description: Visual demonstration of Bubble, Selection, and Insertion Sort

import time

def print_array(arr):
    """Helper function to print array visually"""
    print(" ".join(str(x) for x in arr))
    time.sleep(0.5)  # Delay for visualization


def bubble_sort(arr):
    n = len(arr)
    print("\n--- Bubble Sort Visualization ---")
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print_array(arr)
    print("Sorted Array:", arr)


def selection_sort(arr):
    n = len(arr)
    print("\n--- Selection Sort Visualization ---")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print_array(arr)
    print("Sorted Array:", arr)


def insertion_sort(arr):
    print("\n--- Insertion Sort Visualization ---")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print_array(arr)
        arr[j + 1] = key
        print_array(arr)
    print("Sorted Array:", arr)


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("==== Sorting Visualizer ====")
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)

    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = int(input("Enter your choice (1-3): "))
    original_arr = arr.copy()

    if choice == 1:
        bubble_sort(original_arr)
    elif choice == 2:
        selection_sort(original_arr)
    elif choice == 3:
        insertion_sort(original_arr)
    else:
        print("Invalid choice!")

    print("\n--- Program End ---")
