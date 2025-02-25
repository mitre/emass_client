## eMASS API @mitre/emass_client@3.22.0 Specification

The `@mitre/emass_client@3.22.0` is a TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios)
to implement the [Enterprise Mission Assurance Support Service (eMASS)](https://disa.mil/~/media/Files/DISA/Fact-Sheets/eMASS.pdf)
Representational State Transfer (REST) Application Programming Interface (API) specifications

The generated Node module can be used in the following environments:
Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install @mitre/emass_client@3.22.0 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

## Getting Started
Before accessing any of the endpoints provided by the @mitre/emass_client, we need to configure common axios settings.

### Axios Configuration
All calls utilizing the @mitre/emass_client@3.22.0 need to initialize axios as follows:

```typescript
// Load the necessary modules
import * as fs from 'fs';
import * as https from 'https';
import { Configuration } from "@mitre/emass_client/dist/configuration"
import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from '@mitre/emass_client/node_modules/axios';

// Initialize the configuration interface. The apikey is initialized via axios default headers.
const configuration = new Configuration({
  basePath: 'https://emass-url-instances.com',
});

// Initialize the axios request configuration
const axiosRequestConfig: AxiosRequestConfig = {
  httpsAgent: new https.Agent({
    keepAlive: true,
    rejectUnauthorized: false,
    key: fs.readFileSync("path/to/the/key.pem"),
    cert: fs.readFileSync("path/to/the/client.pem"),
    passphrase: "certificate passphrase",
    port: 443,
  })
}

// Create an axios instances
const axiosInstances: AxiosInstance =  globalAxios.create(axiosRequestConfig);
// Configure the necessary keys (api-key and user-uid)
axiosInstances.defaults.headers.common = {
  "api-key": "the-proper-api-key-value",
  "user-uid": 'the.use.id.information'
};

```
## Documentation for API Endpoints Examples
### Test Connection endpoint
```typescript
// Load the TestApi module
import { TestApi } from '@mitre/emass_client/dist/api';

// Create and initialize a TestApi instances (references code snippet above for proper parameters configurations)
const testApi = new TestApi(configuration, configuration.basePath, axiosInstances);

// Invoke the endpoint 
testApi.testConnection().then((data:any) => {
  console.log("API called successfully. Returned data: " + JSON.stringify(data.data, null,2));
}).catch((error:any) => console.error(error));

```
### Artifacts Export endpoint
This example uses the colorize module to color format the output to the command line.
```typescript
// Load the TestApi module
import { ArtifactsExportApi } from '@mitre/emass_client/dist/api';
import colorize from 'json-colorizer';

// Create and initialize a ArtifactsExportApi instances (references Axios Configuration for proper parameters configurations)
const exportArtifacts = new ArtifactsExportApi(configuration, configuration.basePath, axiosInstances);

// Invoke the endpoint 
exportArtifacts.getSystemArtifactsExport(34, "artifact.txt").then((response:any) => {
  console.log(colorize(JSON.stringify(response.data, null,2)));
}).catch((error:any) => console.error(colorize(JSON.stringify(error.response.data,null,2))));

```