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

from emass_client.models.systems import Systems

class TestSystems(unittest.TestCase):
    """Systems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Systems:
        """Test Systems
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Systems`
        """
        model = Systems()
        if include_optional:
            return Systems(
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
                security_controls_assessor_executive_summary = 'Executive Summary of the system's Security Controls Assessor',
                risk_review_executive_summary = 'Executive Summary of the system's Risk Review',
                terms_for_auth = 'Terms/Conditions to maintain a valid ATO',
                security_plan_approval_status = 'Approved',
                security_plan_approval_date = 1638741660,
                mission_criticality = 'Mission Support (MS)',
                geographical_association = 'VA Operated IS',
                system_ownership_controlled = 'Region 1',
                governing_mission_area = 'DoD portion of the Intelligence MA (DIMA)',
                primary_functional_area = 'Health/Medical',
                secondary_functional_area = 'Logistics',
                primary_control_set = 'NIST SP 800-53 Revision 4',
                confidentiality = 'Low',
                integrity = 'Moderate',
                availability = 'High',
                applied_overlays = 'Classified Information; Privacy',
                applied_stigs = 'Active_Directory_Domain',
                rmf_activity = 'Maintain ATO and conduct reviews',
                cross_domain_ticket = 'Cross Domain Ticket test',
                ditpr_don_id = '5910, 1234, 8765',
                mac = 'II',
                dod_confidentiality = 'Public',
                contingency_plan_required = True,
                contingency_plan_artifact = 'ContingencyPlanTest.pdf',
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
                privacy_impact_assessment_required = True,
                privacy_impact_assessment_status = 'Not Started',
                privacy_impact_assessment_date = 1622048629,
                privacy_impact_assessment_artifact = 'PIATest.pdf',
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
                authorization_to_connect_status = 'Decommissioned',
                is_saa_s = True,
                is_paa_s = False,
                is_iaa_s = True,
                other_service_models = 'Test Other Service',
                need_date = 1638741660,
                overall_risk_score = 'Moderate',
                is_hrr = False,
                connectivity_authorization_date = 1638741660,
                connectivity_authorization_termination_date = 1638741660,
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
                acquisition_category = 'I',
                software_category = 'Government Off-The-Shelf Software (GOTS)',
                cybersecurity_service_provider = 'NIPR',
                cybersecurity_service_provider_exception_justification = 'Exception justification',
                maximum_tolerable_downtime = 'Immediate',
                recovery_time_objective = 'Mission Critical: 12 hours',
                recovery_point_objective = 'Mission Critical: 12 hours',
                business_impact_analysis_required = True,
                business_impact_analysis_artifact = 'BIATest.pdf',
                incident_response_plan_required = True,
                incident_response_plan_artifact = 'IRPlanTest.pdf',
                disaster_recovery_plan_required = True,
                disaster_recovery_plan_artifact = 'DRPlanTest.pdf',
                privacy_threshold_analysis_completed = True,
                privacy_threshold_analysis_date = 1715312304,
                privacy_threshold_analysis_artifact = 'PTATest.pdf',
                privacy_act_system_of_records_notice_required = True,
                e_authentication_risk_assessment_required = True,
                e_authentication_risk_assessment_date = 1715312304,
                e_authentication_risk_assessment_artifact = 'EAuthRisk.pdf',
                ipv4_only_assets = 10,
                ipv6_only_assets = 5,
                ipv4_ipv6_dual_stack_assets = 15,
                total_ip_assets = 30,
                originating_organization = 'Originating Organization',
                system_use_justification = 'System EOL within 120 days',
                system_use_justification_artifact = 'SystemUseJustification.pdf"',
                authorization_to_use_status = 'Authority to Use (ATU)',
                reciprocity_acceptance_status = 'Acceptance status content',
                use_authorization_date = 1715312304,
                reciprocity_acceptance_date = 1715312304,
                use_authorization_termination_date = 1715312304,
                reciprocity_acceptance_termination_date = 1715312304,
                terms_conditions_for_use_summary = 'Test ATU Summary',
                terms_conditions_for_reciprocity_summary = 'Test ATU Summary',
                primary_mission_essential_function = False,
                pmef_description = 'Test PMEF Description',
                mission_essential_function = False,
                mef_description = 'Test MEF Description',
                administration = 'Test Administration',
                administration_other_justification = 'Test Administration Justification',
                atc_iatc_granted_date = 1715312304,
                atc_iatc_expiration_date = 1715312304,
                atc_iatc_pending_items = 'Test ATC/IATC Pending Items',
                pending_items_due_date = 1715312304,
                dodinn_system_id = False,
                authorization_to_use_connect_status = 'Authorization',
                use_connect_authorization_date = 1715312304,
                use_connect_authorization_termination_date = 1715312304,
                terms_conditions_for_use_connect_summary = 'Test ATU Summary',
                workstations = 10,
                servers = 5,
                connectivity_ccsd = [
                    emass_client.models.system_ccsd_connectivity.System CCSD Connectivity(
                        ccsd_number = 'CCSD-579', 
                        connectivity = 'Not Yet Authorized', )
                    ]
            )
        else:
            return Systems(
        )
        """

    def testSystems(self):
        """Test Systems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
