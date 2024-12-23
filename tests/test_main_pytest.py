import pytest # noqa F401
from main import calculate_offset

def test_gain():
    offset, message = calculate_offset(20)
    assert offset == -16.67
    assert message == "You need a 16.67% loss to offset your 20% gain"

def test_loss():
    offset, message = calculate_offset(-20)
    assert offset == 25.0
    assert message == "You need a 25.0% gain to offset your 20% loss"

def test_no_change():
    offset, message = calculate_offset(0)
    assert offset == 0.0
    assert message == "You need a 0.0% gain to offset your 0% loss"