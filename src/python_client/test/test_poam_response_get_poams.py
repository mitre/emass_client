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

from emass_client.models.poam_response_get_poams import PoamResponseGetPoams

class TestPoamResponseGetPoams(unittest.TestCase):
    """PoamResponseGetPoams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoamResponseGetPoams:
        """Test PoamResponseGetPoams
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoamResponseGetPoams`
        """
        model = PoamResponseGetPoams()
        if include_optional:
            return PoamResponseGetPoams(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = None
            )
        else:
            return PoamResponseGetPoams(
        )
        """

    def testPoamResponseGetPoams(self):
        """Test PoamResponseGetPoams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
