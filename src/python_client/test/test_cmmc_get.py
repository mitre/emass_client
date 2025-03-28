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

from emass_client.models.cmmc_get import CmmcGet

class TestCmmcGet(unittest.TestCase):
    """CmmcGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmmcGet:
        """Test CmmcGet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmmcGet`
        """
        model = CmmcGet()
        if include_optional:
            return CmmcGet(
                operation = 'UPDATED',
                hq_organization_name = 'Army',
                uei = '9809123',
                osc_name = 'UC Labs',
                highest_level_owner_cage_code = '99D8B',
                cage_codes_in_scope = '89ED9; 99D8B',
                number_of_employees = 100,
                scope = 'Enterprise',
                scope_description = 'Assessment of UC's Lab',
                assessment_standard = 'NIST SP 800-171 Revision 2',
                assessment_id = '41b89528-a7a8-470a-90f4-c3fd1267d6f7',
                cmmc_uid = 'L20000003',
                overall_score = 110,
                cmmc_status = 'Conditional Level 2 (C3PAO)',
                cmmc_status_date = 1715312304,
                cmmc_status_expiration_date = 1715312304
            )
        else:
            return CmmcGet(
        )
        """

    def testCmmcGet(self):
        """Test CmmcGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
