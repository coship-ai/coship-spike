from lantern import total


def test_total():
    assert total([1, 2]) == 3


def test_total_skips_missing_values():
    assert total([1, None, 2]) == 3
