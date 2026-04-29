from __future__ import annotations


def quick_sort(values: list[int]) -> list[int]:
    if not isinstance(values, list):
        raise TypeError("quick_sort expects a list")

    if len(values) <= 1:
        return values.copy()

    pivot = values[0]
    left: list[int] = []
    middle: list[int] = [pivot]
    right: list[int] = []

    for value in values[1:]:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            middle.append(value)

    return quick_sort(left) + middle + quick_sort(right)


def _self_test() -> None:
    cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 5, 5],
        [8, 3, 5, 1, 9, 2, 7, 4, 6, 3, 8],
        [1, 1, 2, 2, 3, 3],
    ]
    for case in cases:
        result = quick_sort(case)
        assert result == sorted(case), f"quick_sort({case}) -> {result}"
        assert len(result) == len(case), f"length mismatch on {case}"


if __name__ == "__main__":
    _self_test()
    demo_values = [8, 3, 5, 1, 9, 2, 7, 4, 6, 3, 8]
    print("before:", demo_values)
    print("after: ", quick_sort(demo_values))
