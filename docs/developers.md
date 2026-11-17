# Developers Instructions

The documentation provided in this repository describes the eMASS REST API structure. It is an OpenAPI (v3.0.3) specification compliant describing and visualizing the eMASS RESTful API web services (endpoints).

The API is documented in YAML and can be viewed utilizing Swagger Editor or Visual Studio Code (VSC) with swagger and yaml extensions.

## Visualizing 
### Viewing the API via Swagger

There are online tool options for viewing and editing OpenAPI compliant RESTfull APIs like the eMASS API documentations. Some of these tools are Swagger Editor or SwaggerHub. 


***Note***: We recommend utilizing the instruction provided here for viewing or editing the eMASS API.

### Generate the API documentation (html)
The generated eMASS API documentation is available in the [eMASS API Specification](https://mitre.github.io/emass_client/docs/redoc/) page

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

## Development Environment
### Setting up Visual Studio Code (VSC)
Install these Extensions (Ctrl+Shift+X):
* YAML ([link](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml))
* Swagger Viewer ([link](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer))
* OpenAPI Swagger Editor ([link](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi))
* Swagger Snippets ([link](https://marketplace.visualstudio.com/items?itemName=adisreyaj.swagger-snippets), optional)

### Setting up PRISM HTTP mock Server
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

Now you can access the mock API endpoints utilizing either CURL or the Swagger Editor. The following curl command invokes the systems endpoint with a path parameter of policy=rmf:
``` node
curl -X GET "http://localhost:4010/api/systems?policy=rmf" -H  "accept: application/json" -H  "api-key: f32516cc-57d3-43f5-9e16-8f86780a4cce" -H  "user-uid: 1647389405"
```
**Note:** The API expects an api-key and user-uid in the request headers for all endpoint calls. For interacting with the mock server, simply use any arbitrary value for these keys.

## Building an eMASS Client SDK
The API clients are generated utilizing the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) CLI.

**Note:** Currently there are four (4) client SDKs (ruby, typscript-axios, python, and go) that are automatically generated utilizing GitHub action implemented within this repository. They are generated when a push to the main branch occurs and the API specification file has been modified.

The Go client differs from the other three in two ways worth knowing:

- **It is consumed directly from this repository, not from a package registry.** There is no publish workflow for it, because a Go release is a tag. Consumers import `github.com/mitre/emass_client/src/go_client/v3` and resolve a version from tags of the form `src/go_client/v3.22.0`.
- **Its module path is set through `gitRepoId`, not a template.** The Go generator exposes no `moduleName` option; the module path written into `go.mod` is composed from `gitHost/gitUserId/gitRepoId`. Setting `gitRepoId` to `emass_client/src/go_client/v3` therefore produces the correct module path with no mustache override, which is why `src/openapi/templates/go/` contains only a config file. The `/v3` suffix is required by Go for any major version at or above 2, and it tracks the specification's major version as the other clients' package versions do.

### Generate an eMASS Client

#### Using Java executables
Follow these steps to generate an eMASS client for additional supported language provided by the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) CLI:
- Step 1
  
  Install the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator#1---installation) 

  [Download the executable jar](https://github.com/OpenAPITools/openapi-generator#13---download-jar) file and set up a launcher script that will on invocation of the ```openapi-generator-cli```, query the GitHub repository for the most recently released version

- Step 2
  
  Determine if the client desired language is supported by the OpenAPI CLI, invoke the following command to list all current supported client languages:

  ```script
  java -jar openapi-generator-cli list
  ```
- Step 3
  
  To generate the client use the following command ([more details](https://github.com/OpenAPITools/openapi-generator#3---usage)):
  ```script
  java -jar openapi-generator-cli generate -i eMASSRestOpenApi.yaml -g [language] -t templates\directory -c templates\config.json -o output\directory
  ```
  Where:
  
  | Option | Description                                                  |
  | :----: | ------------------------------------------------------------ |
  |   -i   | \<spec file\>, --input-spec \<spec file> location of the OpenAPI spec, as URL or file (required if not loaded via config using -c) |
  |   -g   | \<generator name>, --generator-name \<generator name> generator to use (see list command for list) |
  |   -t   | \<template directory>, --template-dir \<template directory> folder containing the template files |
  |  -c*   | \<configuration file>, --config \<configuration file> Path to configuration file. It can be JSON or YAML |
  |   -o   | \<output directory>, --output \<output directory> where to write the generated files (current dir by default) |
  
  
  \* If file is JSON, the content should have the format
  
      {"optionKey":"optionValue", "optionKey1":"optionValue1"...}
  
    If file is YAML, the content should have the format
  
      optionKey: optionValue. 
  
    Supported options can be different for each language. 
  
    Run config-help -g {generator name} command for language-specific config options.  
  
    For a complete list of available parameters use:
    ```script
    java -jar openapi-generator-cli help generate
    ```
  
- Step 4
  
  To automate the generation process use this [CI action](https://github.com/openapi-generators/openapitools-generator-action):
  ```
  openapi-generators/openapitools-generator-action@v1
  ```

#### Using Docker 
An OpenAPI Generator CLI Docker Image solution is available and documented here as a [Public Pre-built Docker image](https://github.com/OpenAPITools/openapi-generator#16---docker).

Available options are:

- Use the official CLI
    ```
    docker pull openapitools/openapi-generator-cli
    ```
 - Run openapi-generator as a web service
    ```
    docker pull openapitools/openapi-generator-online
    docker run -d -e GENERATOR_HOST=http://12.34.56.78 -p 80:8080 openapitools/openapi-generator-online
    ```
      (where 12.34.56.78 is your server IP address)

To generate a client this way, run the following from the repository root, substituting the language:

```script
docker run --rm -v "$PWD:/local" openapitools/openapi-generator-cli:v7.27.0 \
  generate -i /local/docs/eMASSRestOpenApi.yaml \
           -g [language] \
           -c /local/src/openapi/templates/[language]/[language]-generator-config.json \
           -o /local/[language]-client
```

Then move the result into place as `generate-clients.yml` does, for example for Go:

```script
rm -R src/go_client && mv go-client src/go_client
```

Pin the image tag so a local run is reproducible. Note that the GitHub action used by `generate-clients.yml` does not pin a generator version, so a client regenerated in CI may differ from one generated locally against a pinned tag.


---

NOTICE

© 2020 The MITRE Corporation.

Approved for Public Release; Distribution Unlimited. Case Number 18-3678.
NOTICE

MITRE hereby grants express written permission to use, reproduce, distribute, modify, and otherwise leverage this software to the extent permitted by the licensed terms provided in the LICENSE.md file included with this project.
NOTICE

This software was produced for the U. S. Government under Contract Number HHSM-500-2012-00008I, and is subject to Federal Acquisition Regulation Clause 52.227-14, Rights in Data-General.

No other use other than that granted to the U. S. Government, or to those acting on behalf of the U. S. Government under that Clause is authorized without the express written permission of The MITRE Corporation. DISA STIGs are published by DISA, see: https://public.cyber.mil/privacy-security/
