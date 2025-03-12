import Levenshtein

from apps.main.services.redis_service import RedisService


class DistanceCalculatorService:
    @staticmethod
    def calculate(words: list[str], library_mode: bool = False) -> int:
        cached_data = RedisService.get_cache(words)
        if cached_data is not None:
            return cached_data
        result = (
            Levenshtein.distance(*words)
            if library_mode
            else DistanceCalculatorService._calculate(*words)
        )
        RedisService.set_cache(words, result)

        return result

    @staticmethod
    def _calculate(word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        distance_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:
                    distance_table[i][j] = j
                elif j == 0:
                    distance_table[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    distance_table[i][j] = distance_table[i - 1][j - 1]
                else:
                    distance_table[i][j] = 1 + min(
                        distance_table[i - 1][j],
                        distance_table[i][j - 1],
                        distance_table[i - 1][j - 1],
                    )

        return distance_table[len1][len2]
