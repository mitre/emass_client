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
import datetime

from emass_client.models.containers_resources_post_delete import ContainersResourcesPostDelete  # noqa: E501

class TestContainersResourcesPostDelete(unittest.TestCase):
    """ContainersResourcesPostDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContainersResourcesPostDelete:
        """Test ContainersResourcesPostDelete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContainersResourcesPostDelete`
        """
        model = ContainersResourcesPostDelete()  # noqa: E501
        if include_optional:
            return ContainersResourcesPostDelete(
                container_id = 'command-control',
                success = True,
                system_id = 35,
                errors = [
                    key:value
                    ]
            )
        else:
            return ContainersResourcesPostDelete(
        )
        """

    def testContainersResourcesPostDelete(self):
        """Test ContainersResourcesPostDelete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()