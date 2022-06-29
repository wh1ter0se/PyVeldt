from PyVeldt.subsystems.fadecandy import FadeCandy as fc
from PyVeldt.subsystems.LEDs import Strip as strip

def test_fadecandy():
    fadecandy = fc.FadeCandy()

def test_add_strip():
    fadecandy = fc.FadeCandy()
    test_strip = strip.Strip(label='test_strip', lengths=[42])
    fadecandy.add_strip(0, test_strip)
    