=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client certificate.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.3
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 6.0.1-SNAPSHOT

=end

require 'spec_helper'
require 'json'

# Unit tests for EmassClient::MilestonesApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'MilestonesApi' do
  before do
    # run before each test
    @api_instance = EmassClient::MilestonesApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of MilestonesApi' do
    it 'should create an instance of MilestonesApi' do
      expect(@api_instance).to be_instance_of(EmassClient::MilestonesApi)
    end
  end

  # unit tests for add_milestone_by_system_id_and_poam_id
  # Add milestones to one or many POA&amp;M items in a system
  # Adds a milestone for given &#x60;systemId&#x60; and &#x60;poamId&#x60; path parameters  **Request Body Required Fields** - &#x60;description&#x60; - &#x60;scheduledCompletionDate&#x60;
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param request_body Add milestones to an existing system poam
  # @param [Hash] opts the optional parameters
  # @return [MilestoneResponsePost]
  describe 'add_milestone_by_system_id_and_poam_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_milestone
  # Remove milestones in a system for one or many POA&amp;M items
  # Remove the POA&amp;M matching &#x60;systemId&#x60; and &#x60;poamId&#x60; for path parameters and &#x60;milstoneId&#x60; provide in the Requst Body  **Notes**&lt;br&gt; To delete a milestone the record must be inactive by having the field isActive set to false (&#x60;isActive&#x3D;false&#x60;).
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param milestones_request_delete_body_inner Delete the given Milestone Id
  # @param [Hash] opts the optional parameters
  # @return [MilestonesPutPostDelete]
  describe 'delete_milestone test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_system_milestones_by_poam_id
  # Get milestones in one or many POA&amp;M items in a system
  # Returns system containing milestones for matching parameters.
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :scheduled_completion_date_start **Date Started**: Filter query by the scheduled completion start date (Unix date format).
  # @option opts [String] :scheduled_completion_date_end **Date Ended**: Filter query by the scheduled completion start date (Unix date format).
  # @return [MilestoneResponseGet]
  describe 'get_system_milestones_by_poam_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_system_milestones_by_poam_id_and_milestone_id
  # Get milestone by ID in POA&amp;M item in a system
  # Returns systems containing milestones for matching parameters.
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param milestone_id **Milestone Id**: The unique milestone record identifier.
  # @param [Hash] opts the optional parameters
  # @return [MilestoneResponseGetMilestone]
  describe 'get_system_milestones_by_poam_id_and_milestone_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_milestone_by_system_id_and_poam_id
  # Update one or many POA&amp;M items in a system
  # Updates a milestone for given &#x60;systemId&#x60; and &#x60;poamId&#x60; path parameters  **Request Body Required Fields** - &#x60;milestoneId&#x60; - &#x60;description&#x60; - &#x60;scheduledCompletionDate&#x60;
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param request_body Update milestones for an existing system poam
  # @param [Hash] opts the optional parameters
  # @return [MilestoneResponsePut]
  describe 'update_milestone_by_system_id_and_poam_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
