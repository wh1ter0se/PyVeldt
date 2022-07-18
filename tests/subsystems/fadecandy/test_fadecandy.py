from PyVeldt.subsystems import FadeCandy as fc
from PyVeldt.subsystems import LEDStrip as strip
import pytest

def test_fadecandy():
    fadecandy = fc.FadeCandy()

def test_add_strip():
    fadecandy = fc.FadeCandy()
    test_strip = strip.Strip(label='test_strip', lengths=[42])
    fadecandy.add_strip(3, test_strip)

    assert fadecandy.strips[3] == test_strip
    
def test_overwrite_strip():
    fadecandy = fc.FadeCandy()
    test_strip_A = strip.Strip(label='test_strip_A', lengths=[42])
    test_strip_B = strip.Strip(label='test_strip_B', lengths=[21,21])
    fadecandy.add_strip(0, test_strip_A)

    with pytest.warns(UserWarning):
        fadecandy.add_strip(0, test_strip_B)
    assert fadecandy.strips[0] == test_strip_B

def test_update_pixels():
    fadecandy = fc.FadeCandy()
    test_strip = strip.Strip(label='test_strip', lengths=[42], color_order='RGB')
    fadecandy.add_strip(0, test_strip)

    test_strip.pixels[5] = (1,2,3)
    assert fadecandy.pixels[5] == (0,0,0)
    fadecandy.update_pixels()
    assert fadecandy.pixels[5] == (1,2,3)