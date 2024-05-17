## Enterprise Mission Assurance Support Service (eMASS)
eMASS is a government owned web-based application with a broad range of services for comprehensive fully integrated cybersecurity management. Features include dashboard reporting, controls scorecard measurement, and the generation of a system security authorization package. eMASS provides an integrated suite of authorization capabilities and prevents cyber attacks by establishing strict process control mechanisms for obtaining authorization decisions.

>This document provides instruction on how to register the eMASS API ([eMASSer](https://mitre.github.io/emasser/)) to use with an eMASS Web-Based Application.

### INTRODUCTION
The Enterprise Mission Assurance Support Service (eMASS) web Application 
Programming Interface (API) enables users to perform assessments and complete actions associated with system records.

### GETTING STARTED
#### REGISTER EXTERNAL APPLICATION
Authentication requires a PKI-valid/trusted client certificate and an API key. To obtain an 
API key, client applications submit an API client registration [POST] to {url}/api/api-key.
Every call to the eMASS API will require the use of your client certificate and API key.
The API key must be provided in the request header for all endpoint calls (“api-key”).
If the API receives an untrusted certificate, a 403 forbidden response code will be 
returned. If an invalid api-key or combination of client certificate and api-key from the 
registered account) is received, a 401 unauthorized response code will be returned.

### APPROVE API CLIENT FOR ACTIONABLE REQUESTS
The eMASS web API supports client applications to take actionable requests (PUT, POST, 
DELETE). This section is for actionable requests-only and does not apply to the 
Registration endpoint and all GET requests. 
For actionable requests, some organizations’ policies require an API client application to 
take action on behalf of an existing user account with permissions. Your client 
application’s API account may be setup to require taking action on behalf of a user’s 
account. In this configuration, Users can grant permissions for the client from their eMASS 
User Profile in the API Data Access card by selecting a checkbox for the applicable client 
and clicking [Save].
<div align="center">

![eMASS Data Access Card](/images/emass_data_access_card.png)

</div>

### VERSIONING
Versioning will be specified through a query string parameter (?api-version=1.0) or request 
header (api-version:1.0). If no version is specified, then the system will default to the latest version. 
Available versions will follow the format #.0 and include the latest update from 
that version. E.g. using api-version:1.0 will return results from 1.2 or the latest available 
corresponding 1.# version. All responses will include headers with information about any 
deprecated versions. A deprecated API version will be maintained for 6 months before the 
version is no longer available for use.

The following deprecated API versions are currently available: 
<ul><li>Version 2.3</li></ul>

### REQUEST HEADERS
Available request headers are depicted in the following table:


<table style="width:100%">
    <caption><strong>Available Request Headers</strong></caption>
    <tr>
        <th align=left>key</th>
        <th align=left>Example Value</th>
        <th align=left>Description</th>
    </tr>
    <tr>
        <td style="width:15%">`api-key`</td>
        <td style="width:30%">api-key f32516cc-57d3-43f5-9e16-8f86780a4cce</td>
        <td style="width:55%">This API key must be provided in the request header for all endpoint calls.</td>
    </tr>
    <tr>
        <td>`user-uid`</td>
        <td>1647389405</td>
        <td>
            Unique user identifier for identity provider of the Agency. This key is required in the request header for POST, PUT, and DELETE endpoint calls
            <i>when an API client account is configured to require taking action on behalf of a user account per organizational policy.</i><br>
            <strong>Notes:</strong>
            <ul>
                <li>For DoD, this is the DoD ID Number (EDIPI) on their DoD CAC.</li>
                <li>For certain integrations, the user-uid header is not required.</li>
            </ul>
        </td>
    </tr>
</table>

