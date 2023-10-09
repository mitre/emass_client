# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-09T21:35:37.766947Z[Etc/UTC]

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

from emass_client.api.poam_api import POAMApi  # noqa: E501


class TestPOAMApi(unittest.TestCase):
    """POAMApi unit test stubs"""

    def setUp(self) -> None:
        self.api = POAMApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_poam_by_system_id(self) -> None:
        """Test case for add_poam_by_system_id

        Add one or many POA&M items in a system  # noqa: E501
        """
        pass

    def test_delete_poam(self) -> None:
        """Test case for delete_poam

        Remove one or many POA&M items in a system  # noqa: E501
        """
        pass

    def test_get_system_poams(self) -> None:
        """Test case for get_system_poams

        Get one or many POA&M items in a system  # noqa: E501
        """
        pass

    def test_get_system_poams_by_poam_id(self) -> None:
        """Test case for get_system_poams_by_poam_id

        Get POA&M item by ID in a system  # noqa: E501
        """
        pass

    def test_update_poam_by_system_id(self) -> None:
        """Test case for update_poam_by_system_id

        Update one or many POA&M items in a system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
