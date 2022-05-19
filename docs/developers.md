# Developers Instructions

The documentation provided here is an OpenAPI (v3.0.3) Specification compliant describing, producing, consuming, and visualizing the eMASS RESTful API web services (endpoints) as described by the eMASS REST API (v3.3) document, dated March 26, 2022.

The API is documented in YAML and can be viewed utilizing Swagger Editor or Visual Studio Code (VSC) with swagger and yaml extensions.

### Viewing the API via Swagger

There are online tool options for viewing and editing OpenAPI compliant RESTfull APIs like the eMASS API documentations. Some of these tools are Swagger Editor or SwaggerHub. <strong>We discourage the utilization of any online capability for editing a controlled unclassified API document</strong>.

To install the Swagger Editor offline from its repository follow these [instructions](https://github.com/swagger-api/swagger-editor).

### Generate the API documentation (to view in a web browser-html)
eMASS API documentation can be found [here](https://mitre.github.io/emass_client/docs/redoc/)

To generate the API documentation, viewable on a dependency-free (and nice looking) HTML use the `redoc-cli` command line tool.


Install the tool via `npm`:
```bash
npm install -g redoc-cli
```
To generate the HTML document, use the following command:
```bash
redoc-cli bundle -o ./output/eMASS.html eMASSRestOpenApi.yaml
```

The command above places the generated HTML file (eMASS.html) in a subfolder called output. The command assumes that the eMASSRestApi.yaml is in the current working directory. The generated file can be viewed in any web browser.

### Setting up Visual Studio Code
Install these Extensions (Ctrl+Shift+X):
* YAML ([link](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml))
* Swagger Viewer ([link](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer))
* OpenAPI Swagger Editor ([link](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi))
* Swagger Snippets ([link](https://marketplace.visualstudio.com/items?itemName=adisreyaj.swagger-snippets), optional)

Open the eMASS Rest API file by selecting File -> Open Folder and select the folder containing the eMASSRestApi.yaml file. Open the file into the editor and select the "OpenApi: show preview using default render" (Ctrl+K V)

Once the mock server is running, we can utilize the "Try it Out" on each of the API endpoints to test the API documentation with mock data.

### Using PRISM HTTP mock Server
Install prism (if not installed) via npm:
``` npm
npm install -g @stoplight/prism-cli
```

Run the prism server on the localhost, use the -p parameter to set the port (using 4010)
``` node
prism mock -p 4010 eMASSRestOpenApi.yaml
```

To invoke the mock server interactive use the -d parameter (provides fake responses using x-faker)
``` node
prism mock -d -p 4010 eMASSRestOpenAPI.yaml
```
**Note:**
* The Prism starting commands above assumes that the current path contains the eMASSRestAPI.yaml file
* If using VSC, Prism restarts automatically when the yaml file is modified and saved
* Use `npx` instead of `npm` to install packages locally, but still be able to run them as if they were global

Now you can access the fake API endpoints utilizing either CURL or the Swagger Editor. The following curl command invokes the systems endpoint with a path parameter of policy=rmf:
``` node
curl -X GET "http://localhost:4010/api/systems?policy=rmf" -H  "accept: application/json" -H  "api-key: f32516cc-57d3-43f5-9e16-8f86780a4cce" -H  "user-uid: 1647389405"
```
Note: The API expects the api-key and user-uid headers.

### Build the Client SDK
The API clients are generated utilizing the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) CLI.

**Note:** Currently there are two (2) client SDKs (ruby, and typscript-axios) that are automatically generated utilizing the GitHub action implemented within this repository. The are generated when a push to main occurs and the API specification files has been modified.

---

NOTICE

© 2020 The MITRE Corporation.

Approved for Public Release; Distribution Unlimited. Case Number 18-3678.
NOTICE

MITRE hereby grants express written permission to use, reproduce, distribute, modify, and otherwise leverage this software to the extent permitted by the licensed terms provided in the LICENSE.md file included with this project.
NOTICE

This software was produced for the U. S. Government under Contract Number HHSM-500-2012-00008I, and is subject to Federal Acquisition Regulation Clause 52.227-14, Rights in Data-General.

No other use other than that granted to the U. S. Government, or to those acting on behalf of the U. S. Government under that Clause is authorized without the express written permission of The MITRE Corporation. DISA STIGs are published by DISA, see: https://public.cyber.mil/privacy-security/
