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
import datetime

import emass_client
from emass_client.models.pac_response_post import PacResponsePost  # noqa: E501
from emass_client.rest import ApiException

class TestPacResponsePost(unittest.TestCase):
    """PacResponsePost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PacResponsePost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PacResponsePost`
        """
        model = emass_client.models.pac_response_post.PacResponsePost()  # noqa: E501
        if include_optional :
            return PacResponsePost(
                meta = emass_client.models.ok.OK(
                    code = 200, ), 
                data = [
                    emass_client.models.pac___return_query_from_the_server_for_the_post_call.PAC - return query from the server for the POST call(
                        workflow = 'Assess and Authorize', 
                        success = True, 
                        system_id = 35, 
                        errors = [
                            key:value
                            ], )
                    ]
            )
        else :
            return PacResponsePost(
        )
        """

    def testPacResponsePost(self):
        """Test PacResponsePost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()