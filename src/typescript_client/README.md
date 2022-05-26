## emass_client@1.0.6

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

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

It can be used in both TypeScript and JavaScript. In TypeScript, the definition should be automatically resolved via `package.json`. ([Reference - archive](https://web.archive.org/web/20160412204540/https://www.typescriptlang.org/docs/handbook/typings-for-npm-packages.html))

The latest publishing instruction can be found in the Typescript [handbook](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html) 

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing
After building the package (above step) login into the NPM registry ( [account required](https://www.npmjs.com/signup) ) 

Login with the following command:
```
npm login
``` 

To test that the login was successful, use command ```npm whoami```, the  username for the account is displayed.

Publishing the NPM package is accomplished by executing the following command:
```
npm publish
```

After the publish is done without any error, visit the account used to published in the NPM registry, and verify that the package is there.

### Unpublish NPM
For detailed information on unpublishing an NPM packages visit the [npm-unpuplish docs](https://docs.npmjs.com/cli/v8/commands/npm-unpublish)

```
npm unpublish [<@scope>/]<pkg>[@<version>]
```
References the [npm Unpublish Policy](https://docs.npmjs.com/policies/unpublish) for detail information and restrictions related to unpublishing npm pakages.

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install emass_client@1.0.6 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

## Getting Started
Before accessing any of the endpoints provided by the emass_client, we need to configure common axios settings.

### Axios Configuration
All calls utilizing the emass_client@1.0.6 need to initialize axios as follows:

```typescript
// Load the necessary modules
import * as fs from 'fs';
import * as https from 'https';
import { Configuration } from "emass_client/dist/configuration"
import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'emass_client/node_modules/axios';

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
import { TestApi } from 'emass_client/dist/api';

// Create and initialize a TestApi instances (references Axios Configuration for proper parameters configurations)
const testApi = new TestApi(configuration, configuration.basePath, axiosInstances);

// Invoke the endpoint 
testApi.testConnection().then((response:any) => {
  console.log("API called successfully. Returned data: " + JSON.stringify(response.data, null,2));
}).catch((error:any) => console.error(JSON.stringify(error.response.data,null,2)));

```
### Artifacts Export endpoint
This example uses the colorize module to color format the output to the command line.
```typescript
// Load the TestApi module
import { ArtifactsExportApi } from 'emass_client/dist/api';
import colorize from 'json-colorizer';

// Create and initialize a ArtifactsExportApi instances (references Axios Configuration for proper parameters configurations)
const exportArtifacts = new ArtifactsExportApi(configuration, configuration.basePath, axiosInstances);

// Invoke the endpoint 
exportArtifacts.getSystemArtifactsExport(34, "artifact.txt").then((response:any) => {
  console.log(colorize(JSON.stringify(response.data, null,2)));
}).catch((error:any) => console.error(colorize(JSON.stringify(error.response.data,null,2))));

```
