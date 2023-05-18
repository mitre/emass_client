from emass_client.paths.api_systems_system_id_poams.get import ApiForget
from emass_client.paths.api_systems_system_id_poams.put import ApiForput
from emass_client.paths.api_systems_system_id_poams.post import ApiForpost
from emass_client.paths.api_systems_system_id_poams.delete import ApiFordelete


class ApiSystemsSystemIdPoams(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
