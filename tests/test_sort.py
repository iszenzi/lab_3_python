import pytest
from src.sort import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    heap_sort,
    bucket_sort,
)


class TestBubbleSort:
    def test_bubble_sort(self):
        assert bubble_sort([4, 3, 2, 17, 5, 27, 1]) == [1, 2, 3, 4, 5, 17, 27]
        assert bubble_sort([455, 389, 233, 177, 52, 279, 52]) == [
            52,
            52,
            177,
            233,
            279,
            389,
            455,
        ]

    def test_bubble_negative_sort(self):
        assert bubble_sort([-4, -3, -2, -17, -5, -27, -1]) == [
            -27,
            -17,
            -5,
            -4,
            -3,
            -2,
            -1,
        ]
        assert bubble_sort([-455, -389, -233, -177, -52, -279, -52]) == [
            -455,
            -389,
            -279,
            -233,
            -177,
            -52,
            -52,
        ]

    def test_bubble_single_sort(self):
        assert bubble_sort([1]) == [1]
        assert bubble_sort([52]) == [52]

    def test_bubble_empty_sort(self):
        assert bubble_sort([]) == []

    def test_bubble_float_sort(self):
        with pytest.raises(ValueError) as exc_info:
            bubble_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть целыми числами" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_bubble_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            bubble_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError


class TestQuickSort:
    def test_quick_sort(self):
        assert quick_sort([4, 3, 2, 17, 5, 27, 1]) == [1, 2, 3, 4, 5, 17, 27]
        assert quick_sort([455, 389, 233, 177, 52, 279, 52]) == [
            52,
            52,
            177,
            233,
            279,
            389,
            455,
        ]

    def test_quick_negative_sort(self):
        assert quick_sort([-4, -3, -2, -17, -5, -27, -1]) == [
            -27,
            -17,
            -5,
            -4,
            -3,
            -2,
            -1,
        ]
        assert quick_sort([-455, -389, -233, -177, -52, -279, -52]) == [
            -455,
            -389,
            -279,
            -233,
            -177,
            -52,
            -52,
        ]

    def test_quick_single_sort(self):
        assert quick_sort([1]) == [1]
        assert quick_sort([52]) == [52]

    def test_quick_empty_sort(self):
        assert quick_sort([]) == []

    def test_quick_float_sort(self):
        with pytest.raises(ValueError) as exc_info:
            quick_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть целыми числами" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_quick_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            quick_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError


class TestCountingSort:
    def test_counting_sort(self):
        assert counting_sort([4, 3, 2, 17, 5, 27, 1]) == [1, 2, 3, 4, 5, 17, 27]
        assert counting_sort([455, 389, 233, 177, 52, 279, 52]) == [
            52,
            52,
            177,
            233,
            279,
            389,
            455,
        ]

    def test_counting_negative_sort(self):
        assert counting_sort([-4, -3, -2, -17, -5, -27, -1]) == [
            -27,
            -17,
            -5,
            -4,
            -3,
            -2,
            -1,
        ]
        assert counting_sort([-455, -389, -233, -177, -52, -279, -52]) == [
            -455,
            -389,
            -279,
            -233,
            -177,
            -52,
            -52,
        ]

    def test_quick_single_sort(self):
        assert quick_sort([1]) == [1]
        assert quick_sort([52]) == [52]

    def test_quick_empty_sort(self):
        assert quick_sort([]) == []

    def test_quick_float_sort(self):
        with pytest.raises(ValueError) as exc_info:
            quick_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть целыми числами" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_quick_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            quick_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError


class TestRadixSort:
    def test_radix_sort(self):
        assert radix_sort([4, 3, 2, 17, 5, 27, 1]) == [1, 2, 3, 4, 5, 17, 27]
        assert radix_sort([455, 389, 233, 177, 52, 279, 52]) == [
            52,
            52,
            177,
            233,
            279,
            389,
            455,
        ]

    def test_radix_single_sort(self):
        assert radix_sort([1]) == [1]
        assert radix_sort([52]) == [52]

    def test_radix_empty_sort(self):
        assert radix_sort([]) == []

    def test_radix_float_sort(self):
        with pytest.raises(ValueError) as exc_info:
            radix_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть целыми неотрицательными числами" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_radix_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            radix_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_radix_negative_sort(self):
        with pytest.raises(ValueError) as exc_info:
            radix_sort([-1, 2, 3, 4])
        assert "Элементы списка должны быть целыми неотрицательными числами" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError


class TestBucketSort:
    def test_bucket_sort(self):
        assert bucket_sort([0.1, 0.3, 0.2, 0.4, 0.52]) == [0.1, 0.2, 0.3, 0.4, 0.52]
        assert bucket_sort([0.123, 0.32, 0.252, 0.777, 0.444, 0.52, 0.666]) == [
            0.123,
            0.252,
            0.32,
            0.444,
            0.52,
            0.666,
            0.777,
        ]

    def test_bucket_single_sort(self):
        assert bucket_sort([0.1]) == [0.1]
        assert bucket_sort([0.52]) == [0.52]

    def test_bucket_empty_sort(self):
        assert bucket_sort([]) == []

    def test_bucket_not_in_diapozone_sort(self):
        with pytest.raises(ValueError) as exc_info:
            bucket_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть в диапазоне [0, 1)" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_bucket_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            bucket_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_bucket_negative_sort(self):
        with pytest.raises(ValueError) as exc_info:
            bucket_sort([-1, -2, -3, -44])
        assert "Элементы списка должны быть в диапазоне [0, 1)" in str(exc_info.value)
        assert exc_info.type is ValueError


class TestHeapSort:
    def test_heap_sort(self):
        assert heap_sort([4, 3, 2, 17, 5, 27, 1]) == [1, 2, 3, 4, 5, 17, 27]
        assert heap_sort([455, 389, 233, 177, 52, 279, 52]) == [
            52,
            52,
            177,
            233,
            279,
            389,
            455,
        ]

    def test_heap_negative_sort(self):
        assert heap_sort([-4, -3, -2, -17, -5, -27, -1]) == [
            -27,
            -17,
            -5,
            -4,
            -3,
            -2,
            -1,
        ]
        assert heap_sort([-455, -389, -233, -177, -52, -279, -52]) == [
            -455,
            -389,
            -279,
            -233,
            -177,
            -52,
            -52,
        ]

    def test_heap_single_sort(self):
        assert heap_sort([1]) == [1]
        assert heap_sort([52]) == [52]

    def test_heap_empty_sort(self):
        assert heap_sort([]) == []

    def test_heap_float_sort(self):
        with pytest.raises(ValueError) as exc_info:
            heap_sort([1.0, 5.2, 3.14])
        assert "Элементы списка должны быть целыми числами" in str(exc_info.value)
        assert exc_info.type is ValueError

    def test_heap_not_list_sort(self):
        with pytest.raises(ValueError) as exc_info:
            heap_sort("list")
        assert "Аргумент должен быть списком" in str(exc_info.value)
        assert exc_info.type is ValueError
