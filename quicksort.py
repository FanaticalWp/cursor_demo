from __future__ import annotations


def quick_sort(values: list[int]) -> list[int]:
    if not isinstance(values, list):
        raise TypeError("quick_sort expects a list")

    if len(values) <= 1:
        return values.copy()

    pivot = values[0]
    left: list[int] = []
    right: list[int] = []

    for value in values[1:]:
        if value < pivot:
            left.append(value)
        else:
            right.append(value)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    demo_values = [8, 3, 5, 1, 9, 2, 7, 4, 6]
    print("before:", demo_values)
    print("after: ", quick_sort(demo_values))
