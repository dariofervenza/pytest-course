# add here fixtures to be recognized in multiple test modules

# it uses the name of the module to auto load fixtures


import pytest


@pytest.fixture
def one():
    return 1


# FIXTURES WITH SETUP AND CLEAN UP --> USE yield


@pytest.fixture
def with_clean():
    a = "gay"
    yield a
    # whatcomes after the yield is executed after the test ends (eg a connection.close()) --> EVEN IF THE TEST FAILS IT WILL BE EXECUTED
    del a


# SESSION FIXTURES: Make a fixture run once only, if there are multiple tests, it will be executed only in the first one

@pytest.fixture
def run_once(scope="session"):
    # will run only once in the entire test suite
    # pytest will store the return value and inject it on each test that uses the fixture
    # its usefull if you have to read a file, you only do it once
    return "gay"

# SCOPE VALUES: "function" (default), "session", "class", "module" and "package"


# DEFAULT FIXTURES: fixtures predefined in the pytest package --> see Fixtures reference

# eg: monkey patch --> modify classes or other objects

# eg: requests --> metadata about the test