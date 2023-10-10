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

from emass_client.models.cmmc_response_get import CmmcResponseGet  # noqa: E501

class TestCmmcResponseGet(unittest.TestCase):
    """CmmcResponseGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmmcResponseGet:
        """Test CmmcResponseGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmmcResponseGet`
        """
        model = CmmcResponseGet()  # noqa: E501
        if include_optional:
            return CmmcResponseGet(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.cmmc___return_query_from_the_server_for_the_get_call.CMMC - return query from the server for the GET call(
                        operation = 'UPDATED', 
                        hq_organization_name = 'Army', 
                        uei = '9809123', 
                        cage_codes_in_scope = '89ED9; 99D8B', 
                        osc_name = 'UC Labs', 
                        scope = 'Enterprise', 
                        scope_description = 'Assessment of UC's Lab', 
                        awarded_cmmc_level = 'Not Certified', 
                        expiration_date = 1638741660, 
                        assessment_id = '41b89528-a7a8-470a-90f4-c3fd1267d6f7', 
                        model_version = '1.12', 
                        highest_level_cage_code = '99D8B', 
                        certification_unique_id = 'L20000003', 
                        poam = False, 
                        overall_score = 110, 
                        osc_assessment_official_last_name = 'Smith', 
                        osc_assessment_official_first_name = 'John', 
                        osc_assessment_official_email = 'john.smith6.ctr@mail.mil', 
                        osc_assessment_official_title = 'The Boss', 
                        ssps = [
                            emass_client.models.system_role.System Role(
                                ssp_name = 'UC Lab', 
                                ssp_version = '4.3.0', 
                                ssp_date = 1638741660, )
                            ], )
                    ]
            )
        else:
            return CmmcResponseGet(
        )
        """

    def testCmmcResponseGet(self):
        """Test CmmcResponseGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
