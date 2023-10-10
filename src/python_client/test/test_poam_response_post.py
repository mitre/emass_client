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

from emass_client.models.poam_response_post import PoamResponsePost  # noqa: E501

class TestPoamResponsePost(unittest.TestCase):
    """PoamResponsePost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoamResponsePost:
        """Test PoamResponsePost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoamResponsePost`
        """
        model = PoamResponsePost()  # noqa: E501
        if include_optional:
            return PoamResponsePost(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.poam_post_put_del.PoamPostPutDel(
                        system_id = 33, 
                        poam_id = 45, 
                        external_uid = 'd6d98b88-c866-4496-9bd4-de7ba48d0f52', 
                        success = True, 
                        errors = [
                            key:value
                            ], )
                    ]
            )
        else:
            return PoamResponsePost(
        )
        """

    def testPoamResponsePost(self):
        """Test PoamResponsePost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
