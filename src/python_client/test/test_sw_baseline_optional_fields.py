# coding: utf-8

"""
    Enterprise Mission Assurance Support Service (eMASS)

    The eMASS Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.  The eMASS API provides an interface for application to communicate eMASS Services. For information on how to register and use the eMASS API reference the [eMASS API Getting Started](eMASSGettingStarted.md).  Additional information about eMASS can be obtain by contacting the National Industrial Security Program (NISP). Points of Contact are: 

    The version of the OpenAPI document: v3.22
    Contact: disa.global.servicedesk.mbx.ma-ticket-request@mail.mil
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from emass_client.models.sw_baseline_optional_fields import SwBaselineOptionalFields

class TestSwBaselineOptionalFields(unittest.TestCase):
    """SwBaselineOptionalFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwBaselineOptionalFields:
        """Test SwBaselineOptionalFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwBaselineOptionalFields`
        """
        model = SwBaselineOptionalFields()
        if include_optional:
            return SwBaselineOptionalFields(
                software_type = 'COTS Application',
                parent_system = 'Test Parent System',
                subsystem = 'Test Subsystem',
                network = 'Test Network',
                hosting_environment = 'Test Hosting Environment',
                software_dependencies = 'Test Dependencies',
                cryptographic_hash = 'Test Cryptographic Hash 32"',
                in_service_data = 'Test In-Service Data',
                it_budget_uii = 'Test IT Budget Uii',
                fiscal_year = '2021',
                pop_end_date = 1715312304,
                license_or_contract = 'Test License Or Contract 25',
                license_term = 'Test License Term 25',
                cost_per_license = 250.25,
                total_licenses = 100,
                total_license_cost = 2250.25,
                licenses_used = 100,
                license_poc = 'Smith, Joe',
                license_renewal_date = 1715312304,
                license_expiration_date = 1715312304,
                approval_status = 'In Progress',
                release_date = 1715312304,
                maintenance_date = 1715312304,
                retirement_date = 1715312304,
                end_of_life_support_date = 1715312304,
                extended_end_of_life_support_date = 1715312304,
                critical_asset = False,
                location = 'Test Location',
                purpose = 'Test Purpose',
                unsupported_operating_system = False,
                unapproved_software_from_trm = False,
                approved_waiver = False
            )
        else:
            return SwBaselineOptionalFields(
        )
        """

    def testSwBaselineOptionalFields(self):
        """Test SwBaselineOptionalFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
