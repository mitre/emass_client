=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client certificate.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key. The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.3
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.3.0

=end

require 'spec_helper'
require 'json'

# Unit tests for EmassClient::SystemsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'SystemsApi' do
  before do
    # run before each test
    @api_instance = EmassClient::SystemsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of SystemsApi' do
    it 'should create an instance of SystemsApi' do
      expect(@api_instance).to be_instance_of(EmassClient::SystemsApi)
    end
  end

  # unit tests for get_system
  # Get system information for a specific system
  # Returns the system matching provided parameters
  # @param system_id **System Id**: The unique system record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :include_package **Include Package**:  Indicates if additional packages information is retrieved for queried system.
  # @option opts [String] :policy **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information.
  # @return [SystemResponse]
  describe 'get_system test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_systems
  # Get system information
  # Returns all system(s) that match the query parameters
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :include_package **Include Package**:  Indicates if additional packages information is retrieved for queried system.
  # @option opts [String] :registration_type **Registration Type**: Filter record by selected registration type (single value or comma delimited values).  *Available values:* assessAndAuthorize, assessOnly, guest, regular, functional, cloudServiceProvider, commonControlProvider  
  # @option opts [String] :ditpr_id **DITPR ID**: Filter query by DoD Information Technology (IT) Portfolio Repository (DITPR).
  # @option opts [String] :coams_id **COAMS ID**: Filter query by Cyber Operational Attributes Management System (COAMS).
  # @option opts [String] :policy **System Policy**: Filter query by system policy. If no value is specified and more than one policy is available, the default return is the RMF policy information.
  # @option opts [Boolean] :include_ditpr_metrics **Include DITPR**: Indicates if DITPR metrics are retrieved. This query string parameter can only be used in conjunction with the following parameters:&lt;br&gt;   &lt;ul&gt;     &lt;li&gt;registrationType&lt;/li&gt;     &lt;li&gt;policy&lt;/li&gt;   &lt;/ul&gt;
  # @option opts [Boolean] :include_decommissioned **Include Decommissioned Systems**: Indicates if decommissioned systems are retrieved. If no value is specified, the default returns true to include decommissioned systems.
  # @option opts [Boolean] :reports_for_scorecard **DoD Cyber Hygiene Scorecard**: Indicates if the system reports to the DoD Cyber Hygiene Scorecard.
  # @return [SystemsResponse]
  describe 'get_systems test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end