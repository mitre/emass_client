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

from emass_client.models.dashboard_mock_response import DashboardMockResponse  # noqa: E501

class TestDashboardMockResponse(unittest.TestCase):
    """DashboardMockResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardMockResponse:
        """Test DashboardMockResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardMockResponse`
        """
        model = DashboardMockResponse()  # noqa: E501
        if include_optional:
            return DashboardMockResponse(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.object_mock_data.Object mock data(
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
                        is_active = True, )
                    ],
                pagination = emass_client.models.dashboard_mock_response_pagination.DashboardMockResponse_pagination(
                    total_count = 2, 
                    total_pages = 1, 
                    page_index = 2, 
                    page_size = 20000, 
                    prev_page_url = 'https://myfakeurl.reponse.page.com?PreviousPage', 
                    next_page_url = 'https://myfakeurl.reponse.page.com?NextPage', )
            )
        else:
            return DashboardMockResponse(
        )
        """

    def testDashboardMockResponse(self):
        """Test DashboardMockResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
