from project import convert, check_valid_link, get_csv
from tkinter import *
import pytest

def test_check_valid_link():
    assert check_valid_link("https://www.youtube.com/watch?v=jNQXAC9IVRw") == "https://www.youtube.com/watch?v=jNQXAC9IVRw"

def test_convert():
    with pytest.raises(TclError):
        assert convert("https://www.youtube.com/watch?v=jNQXAC9IVRw") == TclError

def test_get_csv():
    assert get_csv("https://www.youtube.com/watch?v=L576AckqIZg") == "successfully written to csv"