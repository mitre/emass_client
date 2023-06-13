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

import emass_client
from emass_client.api.dashboards_api import DashboardsApi  # noqa: E501
from emass_client.rest import ApiException


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self):
        self.api = emass_client.api.dashboards_api.DashboardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_artifacts_details(self):
        """Test case for get_system_artifacts_details

        System Artifacts Details  # noqa: E501
        """
        pass

    def test_get_system_artifacts_summary(self):
        """Test case for get_system_artifacts_summary

        System Artifacts Summary  # noqa: E501
        """
        pass

    def test_get_system_assessment_procedures_details(self):
        """Test case for get_system_assessment_procedures_details

        System Assessment Procedures Details  # noqa: E501
        """
        pass

    def test_get_system_associations_details(self):
        """Test case for get_system_associations_details

        System Associations Details  # noqa: E501
        """
        pass

    def test_get_system_common_integration_status_summary(self):
        """Test case for get_system_common_integration_status_summary

        System CONMON Integration Status  # noqa: E501
        """
        pass

    def test_get_system_control_compliance_summary(self):
        """Test case for get_system_control_compliance_summary

        System Control Compliance Summary  # noqa: E501
        """
        pass

    def test_get_system_hardware_details(self):
        """Test case for get_system_hardware_details

        System Hardware Details  # noqa: E501
        """
        pass

    def test_get_system_hardware_summary(self):
        """Test case for get_system_hardware_summary

        System Hardware Summary  # noqa: E501
        """
        pass

    def test_get_system_poam_details(self):
        """Test case for get_system_poam_details

        System POA&M Details  # noqa: E501
        """
        pass

    def test_get_system_poam_summary(self):
        """Test case for get_system_poam_summary

        System POA&M Summary  # noqa: E501
        """
        pass

    def test_get_system_ports_protocols_details(self):
        """Test case for get_system_ports_protocols_details

        System Ports/Protocols Details  # noqa: E501
        """
        pass

    def test_get_system_ports_protocols_summary(self):
        """Test case for get_system_ports_protocols_summary

        System Ports/Protocols Summary  # noqa: E501
        """
        pass

    def test_get_system_privacy_summary(self):
        """Test case for get_system_privacy_summary

        System Privacy Summary  # noqa: E501
        """
        pass

    def test_get_system_security_control_details(self):
        """Test case for get_system_security_control_details

        System Control Compliance Details  # noqa: E501
        """
        pass

    def test_get_system_sensor_hardware_details(self):
        """Test case for get_system_sensor_hardware_details

        System Sensor Hardware Details  # noqa: E501
        """
        pass

    def test_get_system_sensor_hardware_summary(self):
        """Test case for get_system_sensor_hardware_summary

        System Sensor Hardware Summary  # noqa: E501
        """
        pass

    def test_get_system_software_details(self):
        """Test case for get_system_software_details

        System Software Details  # noqa: E501
        """
        pass

    def test_get_system_software_summary(self):
        """Test case for get_system_software_summary

        System Software Summary  # noqa: E501
        """
        pass

    def test_get_system_status_details(self):
        """Test case for get_system_status_details

        System Status Details  # noqa: E501
        """
        pass

    def test_get_user_system_assignments_details(self):
        """Test case for get_user_system_assignments_details

        User System Assignments Details  # noqa: E501
        """
        pass

    def test_get_va_omb_fsma_saop_summary(self):
        """Test case for get_va_omb_fsma_saop_summary

        VA OMB FISMA SAOP Summary  # noqa: E501
        """
        pass

    def test_get_va_system_a2_summary(self):
        """Test case for get_va_system_a2_summary

        VA System A2.0 Summary  # noqa: E501
        """
        pass

    def test_get_va_system_aa_summary(self):
        """Test case for get_va_system_aa_summary

        VA System A&A Summary  # noqa: E501
        """
        pass

    def test_get_va_system_fisma_invetory_crypto_summary(self):
        """Test case for get_va_system_fisma_invetory_crypto_summary

        VA System FISMA Inventory Crypto Summary  # noqa: E501
        """
        pass

    def test_get_va_system_fisma_invetory_summary(self):
        """Test case for get_va_system_fisma_invetory_summary

        VA System FISMA Inventory Summary  # noqa: E501
        """
        pass

    def test_get_va_system_pl109_reporting_summary(self):
        """Test case for get_va_system_pl109_reporting_summary

        VA System P.L. 109 Reporting Summary  # noqa: E501
        """
        pass

    def test_get_va_system_threat_architecture_details(self):
        """Test case for get_va_system_threat_architecture_details

        VA System Threat Architecture Details  # noqa: E501
        """
        pass

    def test_get_va_system_threat_risk_summary(self):
        """Test case for get_va_system_threat_risk_summary

        VA System Threat Risks Summary  # noqa: E501
        """
        pass

    def test_get_va_system_threat_source_details(self):
        """Test case for get_va_system_threat_source_details

        VA System Threat Sources Details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
