import pytest


def test_thirdTest(secondCheck):
    print("This is the third test")
    assert secondCheck == "pass"