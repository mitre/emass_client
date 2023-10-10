# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.11.0
- Build date: 2023-10-10T00:19:35.596959Z[Etc/UTC]

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

from emass_client.models.dashboard_mock_response_pagination import DashboardMockResponsePagination  # noqa: E501

class TestDashboardMockResponsePagination(unittest.TestCase):
    """DashboardMockResponsePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardMockResponsePagination:
        """Test DashboardMockResponsePagination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardMockResponsePagination`
        """
        model = DashboardMockResponsePagination()  # noqa: E501
        if include_optional:
            return DashboardMockResponsePagination(
                total_count = 2,
                total_pages = 1,
                page_index = 2,
                page_size = 20000,
                prev_page_url = 'https://myfakeurl.reponse.page.com?PreviousPage',
                next_page_url = 'https://myfakeurl.reponse.page.com?NextPage'
            )
        else:
            return DashboardMockResponsePagination(
        )
        """

    def testDashboardMockResponsePagination(self):
        """Test DashboardMockResponsePagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
