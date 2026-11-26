def create_unsorted_array(full_name: str) -> list:

    seen = set()
    unsorted_array = []

    for char in full_name:
        # Exclude symbols, spaces, numbers, etc.
        if char.isalpha():
            letter = char.lower()
            # Discard duplicate letters
            if letter not in seen:
                seen.add(letter)
                unsorted_array.append(letter)

    return unsorted_array


def selection_sort(arr: list) -> list:
    """Sorts the array alphabetically using Selection Sort."""
    sorted_array = arr.copy()
    n = len(sorted_array)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_array[j] < sorted_array[min_index]:
                min_index = j
        # Swap the found minimum letter with the first unsorted element
        sorted_array[i], sorted_array[min_index] = sorted_array[min_index], sorted_array[i]

    return sorted_array


def main() -> None:
    full_name = "ANNALYN CANONIGO SEBIAL"

    # Check if the name contains any symbols (excluding spaces)
    has_symbol = any(not char.isalnum() and not char.isspace() for char in full_name)
    if has_symbol:
        print(f"Excluded '{full_name}': Names with symbols are not allowed.")
        return

    # 1. Unsorted array (duplicates & spaces removed)
    unsorted_array = create_unsorted_array(full_name)

    # 2. Sorted array (using Selection Sort)
    sorted_array = selection_sort(unsorted_array)

    print("Full Name:     ", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)


if __name__ == "__main__":
    main()