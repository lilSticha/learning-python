from working import convert
import pytest

#9:00 AM to 5:00 PM format
def test_first_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_corect_format():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 1:00 PM") == "00:00 to 13:00"
    assert convert("1:00 AM to 1:00 PM") == "01:00 to 13:00"
    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("10 AM to 10 PM") == "10:00 to 22:00"
    assert convert("10 AM to 10 PM") == "10:00 to 22:00"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("2 AM to 2 PM") == "02:00 to 14:00"
    assert convert("3 AM to 3 PM") == "03:00 to 15:00"
    assert convert("4 AM to 4 PM") == "04:00 to 16:00"
    assert convert("5 AM to 5 PM") == "05:00 to 17:00"
    assert convert("6 AM to 6 PM") == "06:00 to 18:00"
    assert convert("7 AM to 7 PM") == "07:00 to 19:00"
    assert convert("8 AM to 8 PM") == "08:00 to 20:00"
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"

def test_the_same_time():
    assert convert("12:00 AM to 12:00 AM") == "00:00 to 00:00"
    assert convert("12 AM to 12 AM") == "00:00 to 00:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("12 PM to 12 PM") == "12:00 to 12:00"

def test_same_time_with_different_format():
    assert convert("12:00 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 PM to 12:00 AM") == "12:00 to 00:00"

def test_different_time_with_same_format():
    #AM to AM
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("9:00 AM to 10:00 AM") == "09:00 to 10:00"
    assert convert("9 AM to 10:00 AM") == "09:00 to 10:00"
    assert convert("9:00 AM to 10 AM") == "09:00 to 10:00"
    #PM to PM
    assert convert("9 PM to 10 PM") == "21:00 to 22:00"
    assert convert("9:00 PM to 10:00 PM") == "21:00 to 22:00"
    assert convert("9 PM to 10:00 PM") == "21:00 to 22:00"
    assert convert("9:00 PM to 10 PM") == "21:00 to 22:00"




def test_negative_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    #invalid minute value 
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 5:1 PM")
    with pytest.raises(ValueError):
        convert("12:01 AM to 5:61 PM")
    #invalid hour value
    with pytest.raises(ValueError):
        convert("12 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("1 AM to 14 PM")
    with pytest.raises(ValueError):
        convert("14 AM to 14 PM")
    # invalid format
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 6:00 PM")
    with pytest.raises(ValueError):
        convert("12 am to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12 AM to 5:00 pm")
    with pytest.raises(ValueError):
        convert("12 am to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12 am to 5:00")
    with pytest.raises(ValueError):
        convert("12 to 5:00")

    

    
