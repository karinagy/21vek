import pytest

from apps.main.services.distance_calculator import DistanceCalculatorService


@pytest.mark.parametrize(
    "words, distance",
    [
        (["karinka", "mandarinka"], 4),
        (["love", "low"], 2),
        (["hello", "hello"], 0),
        (["abc", "cba"], 2),
        (["", "test"], 4),
        (["test", ""], 4),
        (["", ""], 0),
    ],
)
def test_custom_levenshtein_algorithm(words, distance):
    result = DistanceCalculatorService._calculate(*words)
    assert (
        result == distance
    ), f"Ошибка с пересчетом расстояния для слов  {words}. Пересчитанное расстояние - {result}, ожидаемое расстояние - {distance}"
