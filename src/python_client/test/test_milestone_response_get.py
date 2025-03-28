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

from emass_client.models.milestone_response_get import MilestoneResponseGet

class TestMilestoneResponseGet(unittest.TestCase):
    """MilestoneResponseGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MilestoneResponseGet:
        """Test MilestoneResponseGet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MilestoneResponseGet`
        """
        model = MilestoneResponseGet()
        if include_optional:
            return MilestoneResponseGet(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.milestones___return_query_from_the_server_for_the_get_call.Milestones - return query from the server for the GET call(
                        system_id = 830, 
                        milestone_id = 19, 
                        poam_id = 45, 
                        description = 'Description text', 
                        scheduled_completion_date = 1715312304, 
                        review_status = 'Under Review', 
                        created_by = 'Smith, John', 
                        created_date = 1715312304, )
                    ]
            )
        else:
            return MilestoneResponseGet(
        )
        """

    def testMilestoneResponseGet(self):
        """Test MilestoneResponseGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
