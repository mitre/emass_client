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

from emass_client.models.milestone_response_post import MilestoneResponsePost  # noqa: E501

class TestMilestoneResponsePost(unittest.TestCase):
    """MilestoneResponsePost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MilestoneResponsePost:
        """Test MilestoneResponsePost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MilestoneResponsePost`
        """
        model = MilestoneResponsePost()  # noqa: E501
        if include_optional:
            return MilestoneResponsePost(
                meta = emass_client.models.ok.OK(
                    code = 200, ),
                data = [
                    emass_client.models.milestones_put_post_delete.MilestonesPutPostDelete(
                        system_id = 35, 
                        poam_id = 45, 
                        milestone_id = 77, 
                        external_uid = 'd6d98b88-c866-4496-9bd4-de7ba48d0f52', 
                        success = True, 
                        errors = [
                            key:value
                            ], )
                    ]
            )
        else:
            return MilestoneResponsePost(
        )
        """

    def testMilestoneResponsePost(self):
        """Test MilestoneResponsePost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
