import random
import string

import pytest

from challanges.url_shortner import (
    UrlShortener,
    NoMoreUrlsError,
    UnknownUrlError,
)


def generate_random_strings(n, length):
    random_strings = []
    for _ in range(n):
        random_str = "".join(
            random.choices(string.ascii_letters + string.digits, k=length)
        )
        random_strings.append(random_str)
    return random_strings


class TestUrlShortener:
    def setup_method(self):
        self.short_url_pool = generate_random_strings(100, 7)
        self.shortener = UrlShortener(set(self.short_url_pool))

        self.urls = (
            "https://www.revolut.com/rewards-personalised-cashback-and-discounts/",
            "https://www.revolut.com/rewards/",
            "https://www.revolut.com/business/",
            "https://www.revolut.com/trading/",
        )

    def test_shorten_url(self):
        for url in self.urls:
            short_url = self.shortener.shorten_url(url)
            assert short_url in self.short_url_pool

            original_url = self.shortener.reverse_short_url(short_url)
            assert original_url == url

    def test_max_urls(self):
        max_urls = 100
        urls = [str(i) for i in range(max_urls)]

        for url in urls:
            self.shortener.shorten_url(url)

        extra_url = "this should break"
        with pytest.raises(NoMoreUrlsError):
            self.shortener.shorten_url(extra_url)

    def test_unknown_url(self):
        with pytest.raises(UnknownUrlError):
            self.shortener.reverse_short_url("unknown")
