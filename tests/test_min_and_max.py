import min_and_max


def test_min_and_max():
    res = min_and_max.min_max([1, '42', None, 'Table', 17.3])
    assert res == f"in this list {1, 42, 17} min and max Value are = {min(1)}, {max(42)}"