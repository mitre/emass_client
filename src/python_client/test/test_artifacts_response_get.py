# coding: utf-8

## eMASS API v3.12 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.12
- Package version: 3.12.0
- Build date: 2023-10-10T14:36:02.975730Z[Etc/UTC]

## Requirements.

Python 

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import emass_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import emass_client
```

### Tests

Execute `pytest` to run the tests.

import unittest
import datetime

from emass_client.models.artifacts_response_get import ArtifactsResponseGet  # noqa: E501

class TestArtifactsResponseGet(unittest.TestCase):
    """ArtifactsResponseGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArtifactsResponseGet:
        """Test ArtifactsResponseGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArtifactsResponseGet`
        """
        model = ArtifactsResponseGet()  # noqa: E501
        if include_optional:
            return ArtifactsResponseGet(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.artifacts___return_query_from_the_server_for_the_get_call.Artifacts - return query from the server for the GET call(
                        system_id = 35, 
                        filename = 'AutorizationGuidance.pdf', 
                        is_inherited = True, 
                        is_template = False, 
                        type = 'Policy', 
                        category = 'Change Request', 
                        name = 'E-Authentication Assessment', 
                        description = 'Artifact description text', 
                        reference_page_number = 'Reference page number', 
                        ccis = '000001,000002', 
                        controls = 'AC-8,AC-2(4)', 
                        assessment_procedures = 'AC-1.1', 
                        mime_content_type = 'application/zip', 
                        file_size = '4MB', 
                        expiration_date = 1549036926, 
                        last_reviewed_date = 1549036928, 
                        signed_date = 1549036928, )
                    ]
            )
        else:
            return ArtifactsResponseGet(
        )
        """

    def testArtifactsResponseGet(self):
        """Test ArtifactsResponseGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
