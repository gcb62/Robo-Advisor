# robo_test.py

from robo_advisor import to_usd

def test_usd():
    result1 = to_usd(3.5111111)
    result2 = to_usd(10)
    assert result1 == "$3.51"
    assert result2 == "$10.00"
