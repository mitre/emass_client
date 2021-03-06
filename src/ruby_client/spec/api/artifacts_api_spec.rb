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

# Unit tests for EmassClient::ArtifactsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'ArtifactsApi' do
  before do
    # run before each test
    @api_instance = EmassClient::ArtifactsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of ArtifactsApi' do
    it 'should create an instance of ArtifactsApi' do
      expect(@api_instance).to be_instance_of(EmassClient::ArtifactsApi)
    end
  end

  # unit tests for add_artifacts_by_system_id
  # Add one or many artifacts in a system
  # &lt;strong&gt;Information&lt;/strong&gt;&lt;br&gt; The request body of a POST request through the Artifact Endpoint accepts a single binary file with file extension \&quot;.zip\&quot; only. This accepted .zip file should contain one or more files corresponding to existing artifacts or new artifacts that will be created upon successful receipt. Filename uniqueness throughout eMASS will be enforced by the API.&lt;br&gt;&lt;br&gt; Upon successful receipt of a file, if a file within the .zip is matched via filename to an artifact existing within the application, the file associated with the artifact will be updated. If no artifact is matched via filename to the application, a new artifact will be created with the following default values. Any values not specified below will be blank. &lt;ul&gt;   &lt;li&gt;isTemplate: false&lt;/li&gt;   &lt;li&gt;type: other&lt;/li&gt;   &lt;li&gt;category: evidence&lt;/li&gt; &lt;/ul&gt; To update values other than the file itself, please submit a PUT request.&lt;br&gt;  &lt;strong&gt;Zip file information&lt;/strong&gt;&lt;br&gt; Upload a zip file contain one or more files corresponding to existing artifacts or new artifacts that will be created upon successful receipt.&lt;br&gt;&lt;br&gt; &lt;strong&gt;Business Rules&lt;/strong&gt;&lt;br&gt; Artifact cannot be saved if the file does not have the following file extensions:      .docx,.doc,.txt,.rtf,.xfdl,.xml,.mht,.mh,tml,.html,.htm,.pdf,.mdb,.accdb,.ppt,     .pptx,.xls,.xlsx,.csv,.log,.jpeg,.jpg,.tiff,.bmp,.tif,.png,.gif,.zip,.rar,.msg,     .vsd,.vsw,.vdx,.z{#},.ckl,.avi,.vsdx  Artifact version cannot be saved if an Artifact with the same file name already exist in the system.  Artifact cannot be saved if the file size exceeds 30MB.
  # @param system_id **System Id**: The unique system record identifier.
  # @param zipper 
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :is_template 
  # @option opts [String] :type 
  # @option opts [String] :category 
  # @return [ArtifactsResponsePutPost]
  describe 'add_artifacts_by_system_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_artifact
  # Remove one or many artifacts in a system
  # Remove the Artifact(s) matching &#x60;systemId&#x60; path parameter and request body artifact(s) file name&lt;br&gt;&lt;br&gt; &lt;b&gt;Note:&lt;/b&gt; Multiple files can be deleted by providing multiple file names at the CL (comma delimited)  Example: --files file1.txt, file2.txt
  # @param system_id **System Id**: The unique system record identifier.
  # @param artifacts_request_delete_body_inner Delete artifact files for the given System Id
  # @param [Hash] opts the optional parameters
  # @return [ArtifactsResponseDel]
  describe 'delete_artifact test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_system_artifacts
  # Get one or many artifacts in a system
  # Returns selected artifacts matching parameters to include the file name containing the artifacts.
  # @param system_id **System Id**: The unique system record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :filename **File Name**: The file name (to include file-extension).
  # @option opts [String] :control_acronyms **System Acronym**: Filter query by given system acronym (single or comma separated).
  # @option opts [String] :ccis **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single or comma separated).
  # @option opts [Boolean] :system_only **Systems Only**: Indicates that only system(s) information is retrieved.
  # @return [ArtifactsResponseGet]
  describe 'get_system_artifacts test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_artifact_by_system_id
  # Update one or many artifacts in a system
  # Updates an artifact for given &#x60;systemId&#x60; path parameter&lt;br&gt;&lt;br&gt;  **Request Body Required Fields** - &#x60;filename&#x60; - &#x60;isTemplate&#x60; - &#x60;type&#x60; - &#x60;category&#x60;
  # @param system_id **System Id**: The unique system record identifier.
  # @param request_body See &#x60;information&#x60; above for additional instructions
  # @param [Hash] opts the optional parameters
  # @return [ArtifactsResponsePutPost]
  describe 'update_artifact_by_system_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
