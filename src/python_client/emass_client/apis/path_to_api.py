import typing_extensions

from emass_client.paths import PathValues
from emass_client.apis.paths.api import Api
from emass_client.apis.paths.api_api_key import ApiApiKey
from emass_client.apis.paths.api_systems import ApiSystems
from emass_client.apis.paths.api_systems_system_id import ApiSystemsSystemId
from emass_client.apis.paths.api_system_roles import ApiSystemRoles
from emass_client.apis.paths.api_system_roles_role_category import ApiSystemRolesRoleCategory
from emass_client.apis.paths.api_systems_system_id_controls import ApiSystemsSystemIdControls
from emass_client.apis.paths.api_systems_system_id_test_results import ApiSystemsSystemIdTestResults
from emass_client.apis.paths.api_systems_system_id_poams import ApiSystemsSystemIdPoams
from emass_client.apis.paths.api_systems_system_id_poams_poam_id import ApiSystemsSystemIdPoamsPoamId
from emass_client.apis.paths.api_systems_system_id_poams_poam_id_milestones import ApiSystemsSystemIdPoamsPoamIdMilestones
from emass_client.apis.paths.api_systems_system_id_poams_poam_id_milestones_milestone_id import ApiSystemsSystemIdPoamsPoamIdMilestonesMilestoneId
from emass_client.apis.paths.api_systems_system_id_artifacts import ApiSystemsSystemIdArtifacts
from emass_client.apis.paths.api_systems_system_id_artifacts_export import ApiSystemsSystemIdArtifactsExport
from emass_client.apis.paths.api_systems_system_id_approval_cac import ApiSystemsSystemIdApprovalCac
from emass_client.apis.paths.api_systems_system_id_approval_pac import ApiSystemsSystemIdApprovalPac
from emass_client.apis.paths.api_cmmc_assessments import ApiCmmcAssessments
from emass_client.apis.paths.api_systems_system_id_static_code_scans import ApiSystemsSystemIdStaticCodeScans
from emass_client.apis.paths.api_workflows_definitions import ApiWorkflowsDefinitions
from emass_client.apis.paths.api_workflows_instances import ApiWorkflowsInstances
from emass_client.apis.paths.api_workflows_instances_workflow_instance_id import ApiWorkflowsInstancesWorkflowInstanceId
from emass_client.apis.paths.api_systems_system_id_cloud_resource_results import ApiSystemsSystemIdCloudResourceResults
from emass_client.apis.paths.api_systems_system_id_container_scan_results import ApiSystemsSystemIdContainerScanResults
from emass_client.apis.paths.api_dashboards_system_status_details import ApiDashboardsSystemStatusDetails
from emass_client.apis.paths.api_dashboards_system_control_compliance_summary import ApiDashboardsSystemControlComplianceSummary
from emass_client.apis.paths.api_dashboards_system_security_controls_details import ApiDashboardsSystemSecurityControlsDetails
from emass_client.apis.paths.api_dashboards_system_assessment_procedures_details import ApiDashboardsSystemAssessmentProceduresDetails
from emass_client.apis.paths.api_dashboards_system_poam_summary import ApiDashboardsSystemPoamSummary
from emass_client.apis.paths.api_dashboards_system_poam_details import ApiDashboardsSystemPoamDetails
from emass_client.apis.paths.api_dashboards_system_artifacts_summary import ApiDashboardsSystemArtifactsSummary
from emass_client.apis.paths.api_dashboards_system_artifacts_details import ApiDashboardsSystemArtifactsDetails
from emass_client.apis.paths.api_dashboards_system_hardware_summary import ApiDashboardsSystemHardwareSummary
from emass_client.apis.paths.api_dashboards_system_hardware_details import ApiDashboardsSystemHardwareDetails
from emass_client.apis.paths.api_dashboards_system_sensor_hardware_summary import ApiDashboardsSystemSensorHardwareSummary
from emass_client.apis.paths.api_dashboards_system_sensor_hardware_details import ApiDashboardsSystemSensorHardwareDetails
from emass_client.apis.paths.api_dashboards_system_ports_protocols_summary import ApiDashboardsSystemPortsProtocolsSummary
from emass_client.apis.paths.api_dashboards_system_ports_protocols_details import ApiDashboardsSystemPortsProtocolsDetails
from emass_client.apis.paths.api_dashboards_system_associations_details import ApiDashboardsSystemAssociationsDetails
from emass_client.apis.paths.api_dashboards_user_system_assignments_details import ApiDashboardsUserSystemAssignmentsDetails
from emass_client.apis.paths.api_dashboards_system_privacy_summary import ApiDashboardsSystemPrivacySummary
from emass_client.apis.paths.api_dashboards_va_omb_fisma_saop_summary import ApiDashboardsVaOmbFismaSaopSummary
from emass_client.apis.paths.api_dashboards_va_system_aa_summary import ApiDashboardsVaSystemAaSummary
from emass_client.apis.paths.api_dashboards_va_system_a2_summary import ApiDashboardsVaSystemA2Summary
from emass_client.apis.paths.api_dashboards_va_system_pl_109_reporting_summary import ApiDashboardsVaSystemPl109ReportingSummary
from emass_client.apis.paths.api_dashboards_va_system_fisma_inventory_summary import ApiDashboardsVaSystemFismaInventorySummary
from emass_client.apis.paths.api_dashboards_va_system_fisma_inventory_crypto_summary import ApiDashboardsVaSystemFismaInventoryCryptoSummary
from emass_client.apis.paths.api_dashboards_va_system_threat_risks_summary import ApiDashboardsVaSystemThreatRisksSummary
from emass_client.apis.paths.api_dashboards_va_system_threat_sources_details import ApiDashboardsVaSystemThreatSourcesDetails
from emass_client.apis.paths.api_dashboards_va_system_threat_architecture_details import ApiDashboardsVaSystemThreatArchitectureDetails

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API: Api,
        PathValues.API_APIKEY: ApiApiKey,
        PathValues.API_SYSTEMS: ApiSystems,
        PathValues.API_SYSTEMS_SYSTEM_ID: ApiSystemsSystemId,
        PathValues.API_SYSTEMROLES: ApiSystemRoles,
        PathValues.API_SYSTEMROLES_ROLE_CATEGORY: ApiSystemRolesRoleCategory,
        PathValues.API_SYSTEMS_SYSTEM_ID_CONTROLS: ApiSystemsSystemIdControls,
        PathValues.API_SYSTEMS_SYSTEM_ID_TESTRESULTS: ApiSystemsSystemIdTestResults,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS: ApiSystemsSystemIdPoams,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID: ApiSystemsSystemIdPoamsPoamId,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID_MILESTONES: ApiSystemsSystemIdPoamsPoamIdMilestones,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID_MILESTONES_MILESTONE_ID: ApiSystemsSystemIdPoamsPoamIdMilestonesMilestoneId,
        PathValues.API_SYSTEMS_SYSTEM_ID_ARTIFACTS: ApiSystemsSystemIdArtifacts,
        PathValues.API_SYSTEMS_SYSTEM_ID_ARTIFACTSEXPORT: ApiSystemsSystemIdArtifactsExport,
        PathValues.API_SYSTEMS_SYSTEM_ID_APPROVAL_CAC: ApiSystemsSystemIdApprovalCac,
        PathValues.API_SYSTEMS_SYSTEM_ID_APPROVAL_PAC: ApiSystemsSystemIdApprovalPac,
        PathValues.API_CMMCASSESSMENTS: ApiCmmcAssessments,
        PathValues.API_SYSTEMS_SYSTEM_ID_STATICCODESCANS: ApiSystemsSystemIdStaticCodeScans,
        PathValues.API_WORKFLOWS_DEFINITIONS: ApiWorkflowsDefinitions,
        PathValues.API_WORKFLOWS_INSTANCES: ApiWorkflowsInstances,
        PathValues.API_WORKFLOWS_INSTANCES_WORKFLOW_INSTANCE_ID: ApiWorkflowsInstancesWorkflowInstanceId,
        PathValues.API_SYSTEMS_SYSTEM_ID_CLOUDRESOURCERESULTS: ApiSystemsSystemIdCloudResourceResults,
        PathValues.API_SYSTEMS_SYSTEM_ID_CONTAINERSCANRESULTS: ApiSystemsSystemIdContainerScanResults,
        PathValues.API_DASHBOARDS_SYSTEMSTATUSDETAILS: ApiDashboardsSystemStatusDetails,
        PathValues.API_DASHBOARDS_SYSTEMCONTROLCOMPLIANCESUMMARY: ApiDashboardsSystemControlComplianceSummary,
        PathValues.API_DASHBOARDS_SYSTEMSECURITYCONTROLSDETAILS: ApiDashboardsSystemSecurityControlsDetails,
        PathValues.API_DASHBOARDS_SYSTEMASSESSMENTPROCEDURESDETAILS: ApiDashboardsSystemAssessmentProceduresDetails,
        PathValues.API_DASHBOARDS_SYSTEMPOAMSUMMARY: ApiDashboardsSystemPoamSummary,
        PathValues.API_DASHBOARDS_SYSTEMPOAMDETAILS: ApiDashboardsSystemPoamDetails,
        PathValues.API_DASHBOARDS_SYSTEMARTIFACTSSUMMARY: ApiDashboardsSystemArtifactsSummary,
        PathValues.API_DASHBOARDS_SYSTEMARTIFACTSDETAILS: ApiDashboardsSystemArtifactsDetails,
        PathValues.API_DASHBOARDS_SYSTEMHARDWARESUMMARY: ApiDashboardsSystemHardwareSummary,
        PathValues.API_DASHBOARDS_SYSTEMHARDWAREDETAILS: ApiDashboardsSystemHardwareDetails,
        PathValues.API_DASHBOARDS_SYSTEMSENSORHARDWARESUMMARY: ApiDashboardsSystemSensorHardwareSummary,
        PathValues.API_DASHBOARDS_SYSTEMSENSORHARDWAREDETAILS: ApiDashboardsSystemSensorHardwareDetails,
        PathValues.API_DASHBOARDS_SYSTEMPORTSPROTOCOLSSUMMARY: ApiDashboardsSystemPortsProtocolsSummary,
        PathValues.API_DASHBOARDS_SYSTEMPORTSPROTOCOLSDETAILS: ApiDashboardsSystemPortsProtocolsDetails,
        PathValues.API_DASHBOARDS_SYSTEMASSOCIATIONSDETAILS: ApiDashboardsSystemAssociationsDetails,
        PathValues.API_DASHBOARDS_USERSYSTEMASSIGNMENTSDETAILS: ApiDashboardsUserSystemAssignmentsDetails,
        PathValues.API_DASHBOARDS_SYSTEMPRIVACYSUMMARY: ApiDashboardsSystemPrivacySummary,
        PathValues.API_DASHBOARDS_VAOMBFISMASAOPSUMMARY: ApiDashboardsVaOmbFismaSaopSummary,
        PathValues.API_DASHBOARDS_VASYSTEMAASUMMARY: ApiDashboardsVaSystemAaSummary,
        PathValues.API_DASHBOARDS_VASYSTEMA2SUMMARY: ApiDashboardsVaSystemA2Summary,
        PathValues.API_DASHBOARDS_VASYSTEMPL109REPORTINGSUMMARY: ApiDashboardsVaSystemPl109ReportingSummary,
        PathValues.API_DASHBOARDS_VASYSTEMFISMAINVENTORYSUMMARY: ApiDashboardsVaSystemFismaInventorySummary,
        PathValues.API_DASHBOARDS_VASYSTEMFISMAINVENTORYCRYPTOSUMMARY: ApiDashboardsVaSystemFismaInventoryCryptoSummary,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATRISKSSUMMARY: ApiDashboardsVaSystemThreatRisksSummary,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATSOURCESDETAILS: ApiDashboardsVaSystemThreatSourcesDetails,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATARCHITECTUREDETAILS: ApiDashboardsVaSystemThreatArchitectureDetails,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API: Api,
        PathValues.API_APIKEY: ApiApiKey,
        PathValues.API_SYSTEMS: ApiSystems,
        PathValues.API_SYSTEMS_SYSTEM_ID: ApiSystemsSystemId,
        PathValues.API_SYSTEMROLES: ApiSystemRoles,
        PathValues.API_SYSTEMROLES_ROLE_CATEGORY: ApiSystemRolesRoleCategory,
        PathValues.API_SYSTEMS_SYSTEM_ID_CONTROLS: ApiSystemsSystemIdControls,
        PathValues.API_SYSTEMS_SYSTEM_ID_TESTRESULTS: ApiSystemsSystemIdTestResults,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS: ApiSystemsSystemIdPoams,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID: ApiSystemsSystemIdPoamsPoamId,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID_MILESTONES: ApiSystemsSystemIdPoamsPoamIdMilestones,
        PathValues.API_SYSTEMS_SYSTEM_ID_POAMS_POAM_ID_MILESTONES_MILESTONE_ID: ApiSystemsSystemIdPoamsPoamIdMilestonesMilestoneId,
        PathValues.API_SYSTEMS_SYSTEM_ID_ARTIFACTS: ApiSystemsSystemIdArtifacts,
        PathValues.API_SYSTEMS_SYSTEM_ID_ARTIFACTSEXPORT: ApiSystemsSystemIdArtifactsExport,
        PathValues.API_SYSTEMS_SYSTEM_ID_APPROVAL_CAC: ApiSystemsSystemIdApprovalCac,
        PathValues.API_SYSTEMS_SYSTEM_ID_APPROVAL_PAC: ApiSystemsSystemIdApprovalPac,
        PathValues.API_CMMCASSESSMENTS: ApiCmmcAssessments,
        PathValues.API_SYSTEMS_SYSTEM_ID_STATICCODESCANS: ApiSystemsSystemIdStaticCodeScans,
        PathValues.API_WORKFLOWS_DEFINITIONS: ApiWorkflowsDefinitions,
        PathValues.API_WORKFLOWS_INSTANCES: ApiWorkflowsInstances,
        PathValues.API_WORKFLOWS_INSTANCES_WORKFLOW_INSTANCE_ID: ApiWorkflowsInstancesWorkflowInstanceId,
        PathValues.API_SYSTEMS_SYSTEM_ID_CLOUDRESOURCERESULTS: ApiSystemsSystemIdCloudResourceResults,
        PathValues.API_SYSTEMS_SYSTEM_ID_CONTAINERSCANRESULTS: ApiSystemsSystemIdContainerScanResults,
        PathValues.API_DASHBOARDS_SYSTEMSTATUSDETAILS: ApiDashboardsSystemStatusDetails,
        PathValues.API_DASHBOARDS_SYSTEMCONTROLCOMPLIANCESUMMARY: ApiDashboardsSystemControlComplianceSummary,
        PathValues.API_DASHBOARDS_SYSTEMSECURITYCONTROLSDETAILS: ApiDashboardsSystemSecurityControlsDetails,
        PathValues.API_DASHBOARDS_SYSTEMASSESSMENTPROCEDURESDETAILS: ApiDashboardsSystemAssessmentProceduresDetails,
        PathValues.API_DASHBOARDS_SYSTEMPOAMSUMMARY: ApiDashboardsSystemPoamSummary,
        PathValues.API_DASHBOARDS_SYSTEMPOAMDETAILS: ApiDashboardsSystemPoamDetails,
        PathValues.API_DASHBOARDS_SYSTEMARTIFACTSSUMMARY: ApiDashboardsSystemArtifactsSummary,
        PathValues.API_DASHBOARDS_SYSTEMARTIFACTSDETAILS: ApiDashboardsSystemArtifactsDetails,
        PathValues.API_DASHBOARDS_SYSTEMHARDWARESUMMARY: ApiDashboardsSystemHardwareSummary,
        PathValues.API_DASHBOARDS_SYSTEMHARDWAREDETAILS: ApiDashboardsSystemHardwareDetails,
        PathValues.API_DASHBOARDS_SYSTEMSENSORHARDWARESUMMARY: ApiDashboardsSystemSensorHardwareSummary,
        PathValues.API_DASHBOARDS_SYSTEMSENSORHARDWAREDETAILS: ApiDashboardsSystemSensorHardwareDetails,
        PathValues.API_DASHBOARDS_SYSTEMPORTSPROTOCOLSSUMMARY: ApiDashboardsSystemPortsProtocolsSummary,
        PathValues.API_DASHBOARDS_SYSTEMPORTSPROTOCOLSDETAILS: ApiDashboardsSystemPortsProtocolsDetails,
        PathValues.API_DASHBOARDS_SYSTEMASSOCIATIONSDETAILS: ApiDashboardsSystemAssociationsDetails,
        PathValues.API_DASHBOARDS_USERSYSTEMASSIGNMENTSDETAILS: ApiDashboardsUserSystemAssignmentsDetails,
        PathValues.API_DASHBOARDS_SYSTEMPRIVACYSUMMARY: ApiDashboardsSystemPrivacySummary,
        PathValues.API_DASHBOARDS_VAOMBFISMASAOPSUMMARY: ApiDashboardsVaOmbFismaSaopSummary,
        PathValues.API_DASHBOARDS_VASYSTEMAASUMMARY: ApiDashboardsVaSystemAaSummary,
        PathValues.API_DASHBOARDS_VASYSTEMA2SUMMARY: ApiDashboardsVaSystemA2Summary,
        PathValues.API_DASHBOARDS_VASYSTEMPL109REPORTINGSUMMARY: ApiDashboardsVaSystemPl109ReportingSummary,
        PathValues.API_DASHBOARDS_VASYSTEMFISMAINVENTORYSUMMARY: ApiDashboardsVaSystemFismaInventorySummary,
        PathValues.API_DASHBOARDS_VASYSTEMFISMAINVENTORYCRYPTOSUMMARY: ApiDashboardsVaSystemFismaInventoryCryptoSummary,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATRISKSSUMMARY: ApiDashboardsVaSystemThreatRisksSummary,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATSOURCESDETAILS: ApiDashboardsVaSystemThreatSourcesDetails,
        PathValues.API_DASHBOARDS_VASYSTEMTHREATARCHITECTUREDETAILS: ApiDashboardsVaSystemThreatArchitectureDetails,
    }
)
