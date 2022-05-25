=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client certificate.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.3
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 6.0.0-SNAPSHOT

=end

require 'spec_helper'
require 'json'

# Unit tests for EmassClient::ControlsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'ControlsApi' do
  before do
    # run before each test
    @api_instance = EmassClient::ControlsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of ControlsApi' do
    it 'should create an instance of ControlsApi' do
      expect(@api_instance).to be_instance_of(EmassClient::ControlsApi)
    end
  end

  # unit tests for get_system_controls
  # Get control information in a system for one or many controls
  # Returns system control information for matching &#x60;systemId&#x60; path parameter
  # @param system_id **System Id**: The unique system record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :acronyms **Acronym**: The system acronym(s) being queried (single value or comma delimited values).
  # @return [ControlsResponseGet]
  describe 'get_system_controls test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_control_by_system_id
  # Update control information in a system for one or many controls
  #  Update a Control for given &#x60;systemId&#x60;&lt;br&gt;  **Request Body Required Fields** - &#x60;acronym&#x60; - &#x60;responsibleEntities&#x60; - &#x60;controlDesignation&#x60; - &#x60;estimatedCompletionDate&#x60; - &#x60;implementationNarrative&#x60;  The following optional fields are required based on the Implementation Status &#x60;implementationStatus&#x60; value&lt;br&gt; | Value                    | Required Fields |--------------------------|--------------------------------------------------- | Planned  or Implemented  | &#x60;estimatedCompletionDate&#x60;, &#x60;responsibleEntities&#x60;, &#x60;slcmCriticality&#x60;, &#x60;slcmFrequency&#x60;, &#x60;slcmMethod&#x60;, &#x60;slcmReporting&#x60;, &#x60;slcmTracking&#x60;, &#x60;slcmComments&#x60; | Not Applicable           | &#x60;naJustification&#x60;, &#x60;responsibleEntities&#x60; | Manually Inherited       | &#x60;commonControlProvider&#x60;, &#x60;estimatedCompletionDate&#x60;, &#x60;responsibleEntities&#x60;, &#x60;slcmCriticality&#x60;, &#x60;slcmFrequency&#x60;, &#x60;slcmMethod&#x60;, &#x60;slcmReporting&#x60;, &#x60;slcmTracking&#x60;, &#x60;slcmComments&#x60;  If the Implementation Status &#x60;implementationStatus&#x60; value is &#x60;Inherited&#x60;, only the following fields can be updated:   - &#x60;controlDesignation&#x60;   - &#x60;commonnControlProvider&#x60;
  # @param system_id **System Id**: The unique system record identifier.
  # @param request_body Update an existing control by Id
  # @param [Hash] opts the optional parameters
  # @return [ControlsResponsePut]
  describe 'update_control_by_system_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end