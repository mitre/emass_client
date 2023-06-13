# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.0
- Build date: 2023-06-13T13:46:18.843637Z[Etc/UTC]

## Requirements.

Python 

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import emass_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import emass_client
```

### Tests

Execute `pytest` to run the tests.

import unittest

import emass_client
from emass_client.api.pac_api import PACApi  # noqa: E501
from emass_client.rest import ApiException


class TestPACApi(unittest.TestCase):
    """PACApi unit test stubs"""

    def setUp(self):
        self.api = emass_client.api.pac_api.PACApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_system_pac(self):
        """Test case for add_system_pac

        Submit system package for review  # noqa: E501
        """
        pass

    def test_get_system_pac(self):
        """Test case for get_system_pac

        Get location of system package in PAC  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
