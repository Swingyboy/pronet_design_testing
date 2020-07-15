import pytest


def test(browser, trader_link):
    browser.get(trader_link[0])
    assert 0