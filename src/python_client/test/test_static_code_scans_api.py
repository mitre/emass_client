# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.1
- Build date: 2023-10-10T02:05:20.537795Z[Etc/UTC]

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

from emass_client.api.static_code_scans_api import StaticCodeScansApi  # noqa: E501


class TestStaticCodeScansApi(unittest.TestCase):
    """StaticCodeScansApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StaticCodeScansApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_static_code_scans_by_system_id(self) -> None:
        """Test case for add_static_code_scans_by_system_id

        Upload static code scans or Clear static code scans  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
