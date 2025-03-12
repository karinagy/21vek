from django.core.cache import cache

from distance_calculator.settings import CACHE_TTL


class RedisService:
    @staticmethod
    def _generate_cache_key(words: list[str]) -> str:
        sorted_words = sorted(words)
        return f"distance:{':'.join(sorted_words)}"

    @staticmethod
    def get_cache(words: list[str]):
        cache_key = RedisService._generate_cache_key(words)
        return cache.get(cache_key)

    @staticmethod
    def set_cache(words: list[str], distance: int):
        cache_key = RedisService._generate_cache_key(words)
        cache.set(cache_key, distance, timeout=CACHE_TTL)
