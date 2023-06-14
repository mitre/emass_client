# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.1
- Build date: 2023-06-13T18:24:16.147147Z[Etc/UTC]

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

import emass_client
from emass_client.models.mock_object import MockObject  # noqa: E501
from emass_client.rest import ApiException

class TestMockObject(unittest.TestCase):
    """MockObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MockObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MockObject`
        """
        model = emass_client.models.mock_object.MockObject()  # noqa: E501
        if include_optional :
            return MockObject(
                poc_organization = 'Army', 
                resources = 'Resource text.', 
                owning_organization = 'Defense Information Systems Agency', 
                secondary_organization = 'ID31', 
                poc_first_name = 'John', 
                poc_last_name = 'Smith', 
                poc_email = 'smith@ah.com', 
                poc_phone_number = '555-555-5555', 
                severity = 'Low', 
                scheduled_completion_date = 1599644800, 
                completion_date = 1505916276, 
                comments = 'Comments text.', 
                is_active = True
            )
        else :
            return MockObject(
        )
        """

    def testMockObject(self):
        """Test MockObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
