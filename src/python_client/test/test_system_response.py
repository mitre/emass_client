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

from emass_client.models.system_response import SystemResponse  # noqa: E501

class TestSystemResponse(unittest.TestCase):
    """SystemResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemResponse:
        """Test SystemResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemResponse`
        """
        model = SystemResponse()  # noqa: E501
        if include_optional:
            return SystemResponse(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = emass_client.models.systems___return_query_from_the_server_for_the_get_call.Systems - return query from the server for the GET call(
                    registration_completion_date = 1638741770, 
                    system_life_cycle_acquisition_phase = 'Pre-Milestone A', 
                    special_type = 'Special Type 1', 
                    special_type_description = 'Test Special Type Description', 
                    mission_portfolio = 'Not Applicable', 
                    is_nnpi = False, 
                    is_rbc = False, 
                    is_waiver = True, 
                    program_office = 'Test Program Office', 
                    vram_id = '12345', 
                    system_id = 33, 
                    policy = 'RMF', 
                    registration_type = 'Assess and Authorize', 
                    name = 'System XYZ', 
                    acronym = 'PM-6', 
                    description = 'This is a test system for the eMASS API documentation', 
                    instance = 'Navy', 
                    owning_organization = 'Defense Information Systems Agency', 
                    secondary_organization = 'ID31', 
                    version_release_no = 'V1', 
                    system_type = 'IS Major Application', 
                    is_nss = True, 
                    is_public_facing = True, 
                    coams_id = 93054, 
                    is_type_authorization = True, 
                    ditpr_id = '30498', 
                    apms_id = '30498', 
                    vasi_id = '30498', 
                    authorization_status = 'Not Yet Authorized', 
                    authorization_date = 1638741660, 
                    authorization_termination_date = 1638741660, 
                    authorization_length = 365, 
                    terms_for_auth = 'Terms/Conditions to maintain a valid ATO', 
                    security_plan_approval_status = 'Approved', 
                    security_plan_approval_date = 1638741660, 
                    mission_criticality = 'Mission Support (MS)', 
                    geographical_association = 'VA Operated IS', 
                    system_ownership = 'Region 1', 
                    governing_mission_area = 'DoD portion of the Intelligence MA (DIMA)', 
                    primary_functional_area = 'Health/Medical', 
                    secondary_functional_area = 'Logistics', 
                    primary_control_set = 'NIST SP 800-53 Revision 4', 
                    confidentiality = 'Low', 
                    integrity = 'Moderate', 
                    availability = 'High', 
                    applied_overlays = 'Classified Information', 
                    rmf_activity = 'Maintain ATO and conduct reviews', 
                    cross_domain_ticket = 'Cross Domain Ticket test', 
                    ditpr_don_id = '5910, 1234, 8765', 
                    mac = 'II', 
                    dod_confidentiality = 'Public', 
                    contingency_plan_tested = True, 
                    contingency_plan_test_date = 1426957321, 
                    security_review_required = True, 
                    security_review_completed = True, 
                    security_review_completion_date = 1531958400, 
                    next_security_review_due_date = 1526957321, 
                    has_open_poam_item = True, 
                    has_open_poam_item90to120_past_scheduled_completion_date = False, 
                    has_open_poam_item120_plus_past_scheudled_completion_date = False, 
                    impact = 'Low', 
                    has_cui = False, 
                    has_pii = False, 
                    has_phi = False, 
                    ppsm_registration_required = 'PPSM registration required', 
                    ppsm_registry_number = 'Test PPSM Registry Number', 
                    ppsm_registration_exemption_justification = 'Exemption justification', 
                    interconnected_information_system_and_identifiers = 'Test', 
                    is_pia_required = True, 
                    pia_status = 'Not Started', 
                    pia_date = 1622048629, 
                    user_defined_field1 = 'Test User-defined Field 1', 
                    user_defined_field2 = 'Test User-defined Field 2', 
                    user_defined_field3 = 'Test User-defined Field 3', 
                    user_defined_field4 = 'Test User-defined Field 4', 
                    user_defined_field5 = 'Test User-defined Field 5', 
                    current_rmf_lifecycle_step = '4 - Assess', 
                    other_information = 'Additional Comments', 
                    reports_for_scorecard = True, 
                    highest_system_data_classification = 'Unclassified', 
                    overall_classification = 'Unclassified', 
                    is_hva = True, 
                    is_financial_management = True, 
                    is_reciprocity = True, 
                    reciprocity_exemption = 'Decommission', 
                    cloud_computing = False, 
                    cloud_type = 'Public', 
                    atc_status = 'Decommissioned', 
                    is_saa_s = True, 
                    is_paa_s = False, 
                    is_iaa_s = True, 
                    other_service_models = 'Test Other Service', 
                    need_date = 1638741660, 
                    overall_risk_score = 'Moderate', 
                    is_hrr = False, 
                    atc_date = 1638741660, 
                    atc_termination_date = 1638741660, 
                    system_development_life_cycle = 'Test Other Service', 
                    is_fisma_reportable = False, 
                    group_tagging = 'Group Tag 1', 
                    group_tag_descriptions = 'Group Tag 1 explanation', 
                    dadms_id = 'DADMS-1', 
                    dadms_expiration_date = 1638751730, 
                    enclave_connectivity = 'NIPR', 
                    environment_type = 'Cloud Computing', 
                    navy_common_control_provider = False, 
                    navy_cloud_broker = 'AWS IL 5', 
                    cloud_broker_emass_id = 2349, 
                    cloud_broker_provisional_authorization_atd = 1638741660, 
                    navy_joint_authorization = False, 
                    nmci_ngen_clins = 'NMCI CLIN', 
                    enterprise_locations = 'All Navy Networks', 
                    whitelist_id = 'DoD DMZ Whitelist', 
                    whitelist_inventory = 'Whitelist document', 
                    cybersecurity_service_provider = 'NIPR', 
                    cybersecurity_service_provider_exception_justification = 'Exception justification', 
                    package = [
                        emass_client.models.pac___return_query_from_the_server_for_the_get_call.PAC - return query from the server for the GET call(
                            workflow = 'Assess and Authorize', 
                            name = 'Package name text', 
                            current_stage_name = 'SCA-R', 
                            current_stage = 4, 
                            total_stages = 6, 
                            days_at_current_stage = 2, )
                        ], 
                    connectivity_ccsd = [
                        emass_client.models.system_ccsd_connectivity.System CCSD Connectivity(
                            ccsd_number = 'CCSD Number', 
                            connectivity = 'Test Connectivity', )
                        ], )
            )
        else:
            return SystemResponse(
        )
        """

    def testSystemResponse(self):
        """Test SystemResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
