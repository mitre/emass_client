# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.8.3
- Build date: 2023-05-22T22:31:52.941872Z[Etc/UTC]

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

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_artifacts_summary(self):
        """Test case for get_system_artifacts_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_assessment_procedures_details(self):
        """Test case for get_system_assessment_procedures_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_associations_details(self):
        """Test case for get_system_associations_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_control_compliance_summary(self):
        """Test case for get_system_control_compliance_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_hardware_details(self):
        """Test case for get_system_hardware_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_hardware_summary(self):
        """Test case for get_system_hardware_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_poam_details(self):
        """Test case for get_system_poam_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_poam_summary(self):
        """Test case for get_system_poam_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_ports_protocols_details(self):
        """Test case for get_system_ports_protocols_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_ports_protocols_summary(self):
        """Test case for get_system_ports_protocols_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_privacy_summary(self):
        """Test case for get_system_privacy_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_security_control_details(self):
        """Test case for get_system_security_control_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_sensor_hardware_details(self):
        """Test case for get_system_sensor_hardware_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_sensor_hardware_summary(self):
        """Test case for get_system_sensor_hardware_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_system_status_details(self):
        """Test case for get_system_status_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_user_system_assignments_details(self):
        """Test case for get_user_system_assignments_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_omb_fsma_saop_summary(self):
        """Test case for get_va_omb_fsma_saop_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_a2_summary(self):
        """Test case for get_va_system_a2_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_aa_summary(self):
        """Test case for get_va_system_aa_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_fisma_invetory_crypto_summary(self):
        """Test case for get_va_system_fisma_invetory_crypto_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_fisma_invetory_summary(self):
        """Test case for get_va_system_fisma_invetory_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_pl109_reporting_summary(self):
        """Test case for get_va_system_pl109_reporting_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_threat_architecture_details(self):
        """Test case for get_va_system_threat_architecture_details

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_threat_risk_summary(self):
        """Test case for get_va_system_threat_risk_summary

        Get dashboard information  # noqa: E501
        """
        pass

    def test_get_va_system_threat_source_details(self):
        """Test case for get_va_system_threat_source_details

        Get dashboard information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
