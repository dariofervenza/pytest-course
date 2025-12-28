# FIXTURES: functions used to setup and cleanup

# any test can call fixtures so they are reusable --> eg: instanciate the class in the fixture

# in test_4.py we can see that every test repeats the line 'accum = Accumulator()' --> this is not ok and can be slved with a fixture (it violates the dont repeat yourself principle)


import pytest

from stuff.accum import Accumulator

# fixtures are special functions that pytests calls before each test --> they will do the "arrange" in the arrange-act-assert pattern