import pytest
from clamps import *

def test_default():
    assert True

def test_ps4js():
    js = PS4Joystick()
    print(dir(js))
    assert not js.valid, "Do you have a joystick connected?"
    js.close()