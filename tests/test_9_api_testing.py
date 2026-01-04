# so far we have seen UNIT tests: they test code

# unit test are small and simple to write: catches low-level bugs at the source (where they are easy to identify). They also run quickly so you can run a vast number


# However, pytest also handles BLACK-BOX tests: they interact directly with a live instance of the software instead of making calls to the product code --> INTEGRATION TESTS / END-TO-END TESTS / SYSTEM TESTS / ACCEPTANCE TESTS / FEATURE TESTS
# EXAMPLES: calling a web API, loading a web page in a browser

# API TESTING is a common form of integration testing --> THERE is a whole course (2 hours) only for API testing, we will only see a small example


import pytest

import requests


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duck_duck_go():
    # arrange steps
    url = "https://api.duckduckgo.com/?q=python+programmin&format=json"
    # act steps
    response = requests.get(url)
    body = response.json()
    # assert steps
    assert response.status_code == 200
    assert "Python" in body["AbstractText"]