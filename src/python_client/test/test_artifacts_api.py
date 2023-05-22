# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.8.3
- Build date: 2023-05-22T22:31:52.941872Z[Etc/UTC]

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

import emass_client
from emass_client.api.artifacts_api import ArtifactsApi  # noqa: E501
from emass_client.rest import ApiException


class TestArtifactsApi(unittest.TestCase):
    """ArtifactsApi unit test stubs"""

    def setUp(self):
        self.api = emass_client.api.artifacts_api.ArtifactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_artifacts_by_system_id(self):
        """Test case for add_artifacts_by_system_id

        Add one or many artifacts in a system  # noqa: E501
        """
        pass

    def test_delete_artifact(self):
        """Test case for delete_artifact

        Remove one or many artifacts in a system  # noqa: E501
        """
        pass

    def test_get_system_artifacts(self):
        """Test case for get_system_artifacts

        Get one or many artifacts in a system  # noqa: E501
        """
        pass

    def test_update_artifact_by_system_id(self):
        """Test case for update_artifact_by_system_id

        Update one or many artifacts in a system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
