# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.12.0
- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]

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

from emass_client.models.cloud_resources_delete import CloudResourcesDelete  # noqa: E501

class TestCloudResourcesDelete(unittest.TestCase):
    """CloudResourcesDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudResourcesDelete:
        """Test CloudResourcesDelete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudResourcesDelete`
        """
        model = CloudResourcesDelete()  # noqa: E501
        if include_optional:
            return CloudResourcesDelete(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.cloud_resources___return_query_from_the_server_for_the_post/delete_calls.Cloud Resources - return query from the server for the POST/DELETE calls(
                        resource_id = '/subscriptions/123456789/sample/resource/namespace/default', 
                        success = True, 
                        system_id = 35, 
                        errors = [
                            key:value
                            ], )
                    ]
            )
        else:
            return CloudResourcesDelete(
        )
        """

    def testCloudResourcesDelete(self):
        """Test CloudResourcesDelete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
