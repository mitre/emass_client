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
import datetime

from emass_client.models.container_resources_delete_body_inner import ContainerResourcesDeleteBodyInner  # noqa: E501

class TestContainerResourcesDeleteBodyInner(unittest.TestCase):
    """ContainerResourcesDeleteBodyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContainerResourcesDeleteBodyInner:
        """Test ContainerResourcesDeleteBodyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContainerResourcesDeleteBodyInner`
        """
        model = ContainerResourcesDeleteBodyInner()  # noqa: E501
        if include_optional:
            return ContainerResourcesDeleteBodyInner(
                container_id = '157ac21c-49b4-4faf-a4ac-bfefd869ba3b'
            )
        else:
            return ContainerResourcesDeleteBodyInner(
        )
        """

    def testContainerResourcesDeleteBodyInner(self):
        """Test ContainerResourcesDeleteBodyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()