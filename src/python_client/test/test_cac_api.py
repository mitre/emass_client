# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.1
- Build date: 2023-05-23T01:07:18.461999Z[Etc/UTC]

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
from emass_client.api.cac_api import CACApi  # noqa: E501
from emass_client.rest import ApiException


class TestCACApi(unittest.TestCase):
    """CACApi unit test stubs"""

    def setUp(self):
        self.api = emass_client.api.cac_api.CACApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_system_cac(self):
        """Test case for add_system_cac

        Submit control to second role of CAC  # noqa: E501
        """
        pass

    def test_get_system_cac(self):
        """Test case for get_system_cac

        Get location of one or many controls in CAC  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
