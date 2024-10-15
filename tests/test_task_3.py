import pytest
import task_3


def test_converted():
    res = task_3.converted([1, '10', 36.6, 'Anja'])
    assert res == [1, 10, 36]


