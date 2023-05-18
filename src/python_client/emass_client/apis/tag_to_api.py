import typing_extensions

from emass_client.apis.tags import TagValues
from emass_client.apis.tags.test_api import TestApi
from emass_client.apis.tags.registration_api import RegistrationApi
from emass_client.apis.tags.systems_api import SystemsApi
from emass_client.apis.tags.system_roles_api import SystemRolesApi
from emass_client.apis.tags.controls_api import ControlsApi
from emass_client.apis.tags.test_results_api import TestResultsApi
from emass_client.apis.tags.poam_api import POAMApi
from emass_client.apis.tags.milestones_api import MilestonesApi
from emass_client.apis.tags.artifacts_api import ArtifactsApi
from emass_client.apis.tags.artifacts_export_api import ArtifactsExportApi
from emass_client.apis.tags.cac_api import CACApi
from emass_client.apis.tags.pac_api import PACApi
from emass_client.apis.tags.cmmc_assessments_api import CMMCAssessmentsApi
from emass_client.apis.tags.static_code_scans_api import StaticCodeScansApi
from emass_client.apis.tags.workflow_definitions_api import WorkflowDefinitionsApi
from emass_client.apis.tags.workflow_instances_api import WorkflowInstancesApi
from emass_client.apis.tags.cloud_resource_results_api import CloudResourceResultsApi
from emass_client.apis.tags.container_scan_results_api import ContainerScanResultsApi
from emass_client.apis.tags.dashboards_api import DashboardsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TEST: TestApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.SYSTEM_ROLES: SystemRolesApi,
        TagValues.CONTROLS: ControlsApi,
        TagValues.TEST_RESULTS: TestResultsApi,
        TagValues.POAM: POAMApi,
        TagValues.MILESTONES: MilestonesApi,
        TagValues.ARTIFACTS: ArtifactsApi,
        TagValues.ARTIFACTS_EXPORT: ArtifactsExportApi,
        TagValues.CAC: CACApi,
        TagValues.PAC: PACApi,
        TagValues.CMMC_ASSESSMENTS: CMMCAssessmentsApi,
        TagValues.STATIC_CODE_SCANS: StaticCodeScansApi,
        TagValues.WORKFLOW_DEFINITIONS: WorkflowDefinitionsApi,
        TagValues.WORKFLOW_INSTANCES: WorkflowInstancesApi,
        TagValues.CLOUD_RESOURCE_RESULTS: CloudResourceResultsApi,
        TagValues.CONTAINER_SCAN_RESULTS: ContainerScanResultsApi,
        TagValues.DASHBOARDS: DashboardsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TEST: TestApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.SYSTEM_ROLES: SystemRolesApi,
        TagValues.CONTROLS: ControlsApi,
        TagValues.TEST_RESULTS: TestResultsApi,
        TagValues.POAM: POAMApi,
        TagValues.MILESTONES: MilestonesApi,
        TagValues.ARTIFACTS: ArtifactsApi,
        TagValues.ARTIFACTS_EXPORT: ArtifactsExportApi,
        TagValues.CAC: CACApi,
        TagValues.PAC: PACApi,
        TagValues.CMMC_ASSESSMENTS: CMMCAssessmentsApi,
        TagValues.STATIC_CODE_SCANS: StaticCodeScansApi,
        TagValues.WORKFLOW_DEFINITIONS: WorkflowDefinitionsApi,
        TagValues.WORKFLOW_INSTANCES: WorkflowInstancesApi,
        TagValues.CLOUD_RESOURCE_RESULTS: CloudResourceResultsApi,
        TagValues.CONTAINER_SCAN_RESULTS: ContainerScanResultsApi,
        TagValues.DASHBOARDS: DashboardsApi,
    }
)
