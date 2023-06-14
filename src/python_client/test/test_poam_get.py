# coding: utf-8

## eMASS API v3.10 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.10
- Package version: 3.10.1
- Build date: 2023-06-14T17:42:15.829833Z[Etc/UTC]

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
from emass_client.models.poam_get import PoamGet  # noqa: E501
from emass_client.rest import ApiException

class TestPoamGet(unittest.TestCase):
    """PoamGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PoamGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoamGet`
        """
        model = emass_client.models.poam_get.PoamGet()  # noqa: E501
        if include_optional :
            return PoamGet(
                external_uid = 'd6d98b88-c866-4496-9bd4-de7ba48d0f52', 
                system_id = 830, 
                poam_id = 45, 
                display_poam_id = 100000010, 
                is_inherited = True, 
                control_acronym = '“AC-3”', 
                cci = '000001,000002', 
                status = 'Completed', 
                review_status = 'Under Review', 
                vulnerability_description = 'Description text', 
                source_ident_vuln = 'Source Indentifying Vulnerability text', 
                security_checks = 'SV-25123r1_rule,2016-A-0279', 
                milestones = [
                    emass_client.models.milestones___return_query_from_the_server_for_the_get_call.Milestones - return query from the server for the GET call(
                        system_id = 830, 
                        milestone_id = 19, 
                        poam_id = 45, 
                        description = 'Description text', 
                        scheduled_completion_date = 1599644800, 
                        review_status = 'Under Review', )
                    ], 
                poc_organization = 'Army', 
                poc_first_name = 'John', 
                poc_last_name = 'Smith', 
                poc_email = 'smith@ah.com', 
                poc_phone_number = '555-555-5555', 
                severity = 'Low', 
                raw_severity = 'I', 
                relevance_of_threat = 'Low', 
                likelihood = 'Moderate', 
                impact = 'High', 
                impact_description = 'Impact Description text', 
                residual_risk_level = 'Very Low', 
                recommendations = 'Recommendations text', 
                resources = 'Resource text.', 
                scheduled_completion_date = 1599644800, 
                completion_date = 1505916276, 
                extension_date = 1505916298, 
                comments = 'Comments text.', 
                mitigation = 'Mitigation text', 
                is_active = True
            )
        else :
            return PoamGet(
        )
        """

    def testPoamGet(self):
        """Test PoamGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
