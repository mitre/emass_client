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

from emass_client.api.controls_api import ControlsApi  # noqa: E501


class TestControlsApi(unittest.TestCase):
    """ControlsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ControlsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_system_controls(self) -> None:
        """Test case for get_system_controls

        Get control information in a system for one or many controls  # noqa: E501
        """
        pass

    def test_update_control_by_system_id(self) -> None:
        """Test case for update_control_by_system_id

        Update control information in a system for one or many controls  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()