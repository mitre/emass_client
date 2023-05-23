# coding: utf-8

## eMASS API v3.9 Specification

The emass_client_api is a Python client that implements the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications.


This Python package was generated from the eMASS API specification:

- API version: v3.9
- Package version: 3.9.1
- Build date: 2023-05-23T01:07:18.461999Z[Etc/UTC]

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

import emass_client
from emass_client.models.workflow_instance_response_get import WorkflowInstanceResponseGet  # noqa: E501
from emass_client.rest import ApiException

class TestWorkflowInstanceResponseGet(unittest.TestCase):
    """WorkflowInstanceResponseGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowInstanceResponseGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowInstanceResponseGet`
        """
        model = emass_client.models.workflow_instance_response_get.WorkflowInstanceResponseGet()  # noqa: E501
        if include_optional :
            return WorkflowInstanceResponseGet(
                meta = emass_client.models.ok.OK(
                    code = 200, ), 
                data = [
                    emass_client.models.workflow_instances___return_query_for_the_get_workflow_instance_by_id.Workflow Instances - return query for the GET workflow instance by ID(
                        workflow_uid = '6f810301-5b3b-4f89-81e7-587fef9142a9', 
                        system_name = 'Test system 1', 
                        workflow_instance_id = 35, 
                        package_name = 'Test RMF Step 1 package', 
                        created_date = 1636124623, 
                        last_edited_date = 1631130837, 
                        last_edited_by = 'john.doe.ctr@mail.mil', 
                        workflow = 'RMF Step 1: Security Category', 
                        version = '4', 
                        current_stage = 'Echelon II', 
                        transitions = [
                            emass_client.models.workflow_instances_transition.Workflow Instances Transition(
                                comments = 'Approved the categorization', 
                                created_by = 'john.doe.ctr@mail.mil', 
                                created_date = 1636124623, 
                                description = 'Submit New Package', 
                                end_stage = 'Submit Categorization', 
                                start_stage = 'Not Started', )
                            ], )
                    ]
            )
        else :
            return WorkflowInstanceResponseGet(
        )
        """

    def testWorkflowInstanceResponseGet(self):
        """Test WorkflowInstanceResponseGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
