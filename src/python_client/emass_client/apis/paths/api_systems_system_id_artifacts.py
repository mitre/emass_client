from emass_client.paths.api_systems_system_id_artifacts.get import ApiForget
from emass_client.paths.api_systems_system_id_artifacts.put import ApiForput
from emass_client.paths.api_systems_system_id_artifacts.post import ApiForpost
from emass_client.paths.api_systems_system_id_artifacts.delete import ApiFordelete


class ApiSystemsSystemIdArtifacts(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
