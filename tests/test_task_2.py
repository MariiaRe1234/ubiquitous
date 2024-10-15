import pytest
import task_2


def test_get_name_original():
    res = task_2.get_name([77, 97, 114, 105, 105, 97])
    assert res == 'Mariia'


@pytest.mark.parametrize('digits, expected_res', [
    ([77, 97, 114, 105, 105, 97], 'Mariia'),
    ([0x4f, 0x6c, 0x65, 0x6b, 0x73, 0x61, 0x6e, 0x64, 0x72], 'Oleksandr'),
    ([10000, ], '✐'),
    ([], ''),
    ([1, 2, 1001], '1001 nights with Scheherazade')
])
def test_get_name(digits, expected_res):
    res = task_2.get_name(digits)
    assert res == expected_res


def test_get_name_wrong_type():
    with pytest.raises(TypeError):
        task_2.get_name(['FFF', ])