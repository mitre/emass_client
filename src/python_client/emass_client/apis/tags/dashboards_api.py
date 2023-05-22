# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.0
- Build date: 2023-05-21T19:48:58.553127800-05:00[America/Chicago]

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

## Getting Started

In your own code, to use this library to connect and interact with emass_client_api,
you can run the following:

```python

import time
import emass_client
from pprint import pprint
```
## Documentation For Authorization

Authentication information is documented in the [emass_client specification GitHub page](https://mitre.github.io/emass_client/docs/redoc/)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in emass_client.apis and emass_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from emass_client.apis.default_api import DefaultApi`
- `from emass_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import emass_client
from emass_client.apis import *
from emass_client.models import *
```
from emass_client.paths.api_dashboards_system_artifacts_details.get import GetSystemArtifactsDetails
from emass_client.paths.api_dashboards_system_artifacts_summary.get import GetSystemArtifactsSummary
from emass_client.paths.api_dashboards_system_assessment_procedures_details.get import GetSystemAssessmentProceduresDetails
from emass_client.paths.api_dashboards_system_associations_details.get import GetSystemAssociationsDetails
from emass_client.paths.api_dashboards_system_control_compliance_summary.get import GetSystemControlComplianceSummary
from emass_client.paths.api_dashboards_system_hardware_details.get import GetSystemHardwareDetails
from emass_client.paths.api_dashboards_system_hardware_summary.get import GetSystemHardwareSummary
from emass_client.paths.api_dashboards_system_poam_details.get import GetSystemPoamDetails
from emass_client.paths.api_dashboards_system_poam_summary.get import GetSystemPoamSummary
from emass_client.paths.api_dashboards_system_ports_protocols_details.get import GetSystemPortsProtocolsDetails
from emass_client.paths.api_dashboards_system_ports_protocols_summary.get import GetSystemPortsProtocolsSummary
from emass_client.paths.api_dashboards_system_privacy_summary.get import GetSystemPrivacySummary
from emass_client.paths.api_dashboards_system_security_controls_details.get import GetSystemSecurityControlDetails
from emass_client.paths.api_dashboards_system_sensor_hardware_details.get import GetSystemSensorHardwareDetails
from emass_client.paths.api_dashboards_system_sensor_hardware_summary.get import GetSystemSensorHardwareSummary
from emass_client.paths.api_dashboards_system_status_details.get import GetSystemStatusDetails
from emass_client.paths.api_dashboards_user_system_assignments_details.get import GetUserSystemAssignmentsDetails
from emass_client.paths.api_dashboards_va_omb_fisma_saop_summary.get import GetVaOmbFsmaSaopSummary
from emass_client.paths.api_dashboards_va_system_a2_summary.get import GetVaSystemA2Summary
from emass_client.paths.api_dashboards_va_system_aa_summary.get import GetVaSystemAaSummary
from emass_client.paths.api_dashboards_va_system_fisma_inventory_crypto_summary.get import GetVaSystemFismaInvetoryCryptoSummary
from emass_client.paths.api_dashboards_va_system_fisma_inventory_summary.get import GetVaSystemFismaInvetorySummary
from emass_client.paths.api_dashboards_va_system_pl_109_reporting_summary.get import GetVaSystemPl109ReportingSummary
from emass_client.paths.api_dashboards_va_system_threat_architecture_details.get import GetVaSystemThreatArchitectureDetails
from emass_client.paths.api_dashboards_va_system_threat_risks_summary.get import GetVaSystemThreatRiskSummary
from emass_client.paths.api_dashboards_va_system_threat_sources_details.get import GetVaSystemThreatSourceDetails


class DashboardsApi(
    GetSystemArtifactsDetails,
    GetSystemArtifactsSummary,
    GetSystemAssessmentProceduresDetails,
    GetSystemAssociationsDetails,
    GetSystemControlComplianceSummary,
    GetSystemHardwareDetails,
    GetSystemHardwareSummary,
    GetSystemPoamDetails,
    GetSystemPoamSummary,
    GetSystemPortsProtocolsDetails,
    GetSystemPortsProtocolsSummary,
    GetSystemPrivacySummary,
    GetSystemSecurityControlDetails,
    GetSystemSensorHardwareDetails,
    GetSystemSensorHardwareSummary,
    GetSystemStatusDetails,
    GetUserSystemAssignmentsDetails,
    GetVaOmbFsmaSaopSummary,
    GetVaSystemA2Summary,
    GetVaSystemAaSummary,
    GetVaSystemFismaInvetoryCryptoSummary,
    GetVaSystemFismaInvetorySummary,
    GetVaSystemPl109ReportingSummary,
    GetVaSystemThreatArchitectureDetails,
    GetVaSystemThreatRiskSummary,
    GetVaSystemThreatSourceDetails,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
