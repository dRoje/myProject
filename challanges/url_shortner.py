import random
from typing import Set, Dict


class UnknownUrlError(Exception):
    pass


class MaxUrlsError(Exception):
    pass


class NoMoreUrlsError(Exception):
    pass


class UrlShortener:
    def __init__(self, short_url_pool: Set[str]) -> None:
        self.url_map: Dict[str, str] = {}
        self.short_url_pool = short_url_pool

        if len(short_url_pool) > 100:
            raise MaxUrlsError()

    def shorten_url(self, long_url: str) -> str:
        """Assign long url to a one of the short urls in the pool. Return short url."""

        taken_short_urls = set(self.url_map.keys())
        free_short_urls = self.short_url_pool - taken_short_urls

        if not free_short_urls:
            raise NoMoreUrlsError()

        short_url = random.choice(list(free_short_urls))

        self.url_map[short_url] = long_url

        return short_url

    def reverse_short_url(self, short_url: str) -> str:
        """Find matching short url in the pool and return it. Raise UnknownUrlError if no mathc."""

        long_url = self.url_map.get(short_url)

        if not long_url:
            raise UnknownUrlError

        return long_url
