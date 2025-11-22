import pytest
from k_length_apart import k_length_apart


@pytest.mark.parametrize("nums,k,expected", [
    ([1,0,0,0,1,0,0,1], 2, True),
    ([1,0,0,1], 2, True),
    ([0,0,0,0], 1, True),
    ([1,1,1,1], 0, True),
    ([1,0,1], 1, True),
    ([1,0,1], 2, False),
    ([1], 1, True),
    ([0,1,0,0,1], 2, True),
])
def test_k_length_apart(nums, k, expected):
    assert k_length_apart(nums, k) is expected


def test_invalid_values():
    # Non-binary values should be ignored by the algorithm design,
    # but we still test behavior (function expects 0/1 inputs).
    with pytest.raises(TypeError):
        k_length_apart(None, 1)
