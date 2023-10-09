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

from emass_client.api.milestones_api import MilestonesApi  # noqa: E501


class TestMilestonesApi(unittest.TestCase):
    """MilestonesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MilestonesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_milestone_by_system_id_and_poam_id(self) -> None:
        """Test case for add_milestone_by_system_id_and_poam_id

        Add milestones to one or many POA&M items in a system  # noqa: E501
        """
        pass

    def test_delete_milestone(self) -> None:
        """Test case for delete_milestone

        Remove milestones in a system for one or many POA&M items  # noqa: E501
        """
        pass

    def test_get_system_milestones_by_poam_id(self) -> None:
        """Test case for get_system_milestones_by_poam_id

        Get milestones in one or many POA&M items in a system  # noqa: E501
        """
        pass

    def test_get_system_milestones_by_poam_id_and_milestone_id(self) -> None:
        """Test case for get_system_milestones_by_poam_id_and_milestone_id

        Get milestone by ID in POA&M item in a system  # noqa: E501
        """
        pass

    def test_update_milestone_by_system_id_and_poam_id(self) -> None:
        """Test case for update_milestone_by_system_id_and_poam_id

        Update one or many POA&M items in a system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
