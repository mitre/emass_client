# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from emass_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TEST = "Test"
    REGISTRATION = "Registration"
    SYSTEMS = "Systems"
    SYSTEM_ROLES = "System Roles"
    CONTROLS = "Controls"
    TEST_RESULTS = "Test Results"
    POAM = "POAM"
    MILESTONES = "Milestones"
    ARTIFACTS = "Artifacts"
    ARTIFACTS_EXPORT = "Artifacts Export"
    CAC = "CAC"
    PAC = "PAC"
    CMMC_ASSESSMENTS = "CMMC Assessments"
    STATIC_CODE_SCANS = "Static Code Scans"
    WORKFLOW_DEFINITIONS = "Workflow Definitions"
    WORKFLOW_INSTANCES = "Workflow Instances"
    CLOUD_RESOURCE_RESULTS = "Cloud Resource Results"
    CONTAINER_SCAN_RESULTS = "Container Scan Results"
    DASHBOARDS = "Dashboards"
