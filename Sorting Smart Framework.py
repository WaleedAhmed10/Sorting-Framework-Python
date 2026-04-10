import heapq

def analyze_and_sort(arr):
    "Smart function that analyzes and sorts any array"    
    if not arr:
        return []
    size = len(arr)    
    out_of_order = 0
    for i in range(size - 1):
        if arr[i] > arr[i + 1]:
            out_of_order += 1
    is_almost_sorted = out_of_order < (size * 0.1)    
    unique_count = len(set(arr))
    has_many_duplicates = (1 - unique_count/size) > 0.3
    
    print(f"\nDATA ANALYSIS:")
    print(f"   Size: {size}")
    print(f"   Almost sorted: {'Yes' if is_almost_sorted else 'No'}")
    print(f"   Many duplicates: {'Yes' if has_many_duplicates else 'No'}")
    
    if size <= 10:
        print(f"Selected: INSERTION SORT (small array)\n")
        return insertion_sort(arr)
    elif is_almost_sorted:
        print(f"Selected: INSERTION SORT (almost sorted)\n")
        return insertion_sort(arr)
    elif has_many_duplicates:
        print(f"Selected: QUICK SORT (handles duplicates)\n")
        return quick_sort(arr)
    else:
        print(f"Selected: MERGE SORT (general purpose)\n")
        return merge_sort(arr)


def insertion_sort(arr):
    "Simple insertion sort"
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def quick_sort(arr):
    "Simple quick sort"
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    "Simple merge sort"
    if len(arr) <= 1:
        return arr.copy()    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print("=" * 60)
print("SMART SORTING FUNCTION")
print("=" * 60)

test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], "Random array")
]

for numbers, description in test_cases:
    print(f"\n{'='*60}")
    print(f"TEST: {description}")
    print(f"Original: {numbers}")
    sorted_result = analyze_and_sort(numbers)
    print(f"Sorted:   {sorted_result}")

print("\n" + "=" * 60)
print("Smart sorting completed!")