#!/usr/bin/python3

from hypothesis import given
from hypothesis.strategies._internal.deferred import DeferredStrategy

from brownie.network.account import Account
from brownie.test import strategy


def test_strategy():
    assert isinstance(strategy("address"), DeferredStrategy)


@given(value=strategy("address"))
def test_given(accounts, value):
    assert value in accounts
    assert isinstance(value, Account)


@given(value=strategy("address", length=3))
def test_length(accounts, value):
    assert accounts.index(value) < 3


def test_repr():
    assert repr(strategy("address")) == "sampled_from(accounts)"
