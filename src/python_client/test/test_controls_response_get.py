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
from emass_client.models.controls_response_get import ControlsResponseGet  # noqa: E501
from emass_client.rest import ApiException

class TestControlsResponseGet(unittest.TestCase):
    """ControlsResponseGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ControlsResponseGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ControlsResponseGet`
        """
        model = emass_client.models.controls_response_get.ControlsResponseGet()  # noqa: E501
        if include_optional :
            return ControlsResponseGet(
                meta = emass_client.models.ok.OK(
                    code = 200, ), 
                data = [
                    emass_client.models.controls___server_returned_data_from_the_get_call.Controls - server returned data from the GET call(
                        system_id = 35, 
                        name = 'System XYZ', 
                        acronym = 'AC-3', 
                        ccis = '000001,000002', 
                        is_inherited = True, 
                        modified_by_overlays = 'Requirements', 
                        included_status = 'Manually', 
                        compliance_status = 'Status', 
                        responsible_entities = 'Unknown', 
                        implementation_status = 'Planned', 
                        common_control_provider = 'DoD', 
                        na_justification = 'System EOL within 120 days', 
                        control_designation = 'Common', 
                        estimated_completion_date = 1638741660, 
                        implementation_narrative = 'Test Imp. Narrative', 
                        slcm_criticality = 'Test Criticality', 
                        slcm_frequency = 'Annually', 
                        slcm_method = 'Automated', 
                        slcm_reporting = 'Test Reporting', 
                        slcm_tracking = 'Test Tracking', 
                        slcm_comments = 'Test SLCM Comments', 
                        severity = 'Low', 
                        vulnerabilty_summary = 'Test Vulnerability Summary', 
                        recommendations = 'Test Recommendations', 
                        relevance_of_threat = 'Low', 
                        likelihood = 'Low', 
                        impact = 'Low', 
                        impact_description = 'Impact text', 
                        residual_risk_level = 'Low', 
                        test_method = 'Test', )
                    ]
            )
        else :
            return ControlsResponseGet(
        )
        """

    def testControlsResponseGet(self):
        """Test ControlsResponseGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()