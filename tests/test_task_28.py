import task_28
import pytest

# Тесты с использованием параметризации
@pytest.mark.parametrize("input_text, expected", [
    ("aeoui", (5, 0)),  # Только гласные
    ("bcdfg", (0, 5)),  # Только согласные
    ("Hello, World!", (3, 7)),  # Смешанный текст с пунктуацией
    ("", (0, 0)),  # Пустая строка
    ("Python! is awesome!", (6, 9)),  # Смешанный текст с гласными, согласными и пунктуацией
    ("12345", (0, 0)),  # Числа считаем как согласные
    ("AaOoEe", (6, 0)),  # Прописные и строчные гласные
    ("Hi there!", (3, 4)),  # Текст с пробелами
])
def test_vowels(input_text, expected):
    assert task_28.vowels(input_text) == expected
