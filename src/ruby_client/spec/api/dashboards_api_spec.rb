=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` endpoint to register the client certificate.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.10
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 7.0.0-SNAPSHOT

=end

require 'spec_helper'
require 'json'

# Unit tests for EmassClient::DashboardsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'DashboardsApi' do
  before do
    # run before each test
    @api_instance = EmassClient::DashboardsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of DashboardsApi' do
    it 'should create an instance of DashboardsApi' do
      expect(@api_instance).to be_instance_of(EmassClient::DashboardsApi)
    end
  end

  # unit tests for get_system_artifacts_details
  # System Artifacts Details
  # Get system Artifacts details information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_artifacts_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_artifacts_summary
  # System Artifacts Summary
  # Get system Artifacts summary information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_artifacts_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_assessment_procedures_details
  # System Assessment Procedures Details
  # Get systems assessement procdures details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_assessment_procedures_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_associations_details
  # System Associations Details
  # Get system associations details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_associations_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_common_integration_status_summary
  # System CONMON Integration Status
  # Get system CONMON integration status dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_common_integration_status_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_control_compliance_summary
  # System Control Compliance Summary
  # Get systems control compliance summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_control_compliance_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_hardware_details
  # System Hardware Details
  # Get system hardware details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_hardware_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_hardware_summary
  # System Hardware Summary
  # Get system hardware summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_hardware_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_poam_details
  # System POA&amp;M Details
  # Get system POA&amp;Ms details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_poam_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_poam_summary
  # System POA&amp;M Summary
  # Get systems POA&amp;Ms summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_poam_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_ports_protocols_details
  # System Ports/Protocols Details
  # Get system ports and protocols details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_ports_protocols_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_ports_protocols_summary
  # System Ports/Protocols Summary
  # Get system ports and protocols summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_ports_protocols_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_privacy_summary
  # System Privacy Summary
  # Get user system privacy summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_privacy_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_security_control_details
  # System Control Compliance Details
  # Get systems security control details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_security_control_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_sensor_hardware_details
  # System Sensor Hardware Details
  # Get system sensor hardware details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_sensor_hardware_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_sensor_hardware_summary
  # System Sensor Hardware Summary
  # Get system sensor hardware summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_sensor_hardware_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_software_details
  # System Software Details
  # Get system software details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_software_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_software_summary
  # System Software Summary
  # Get system software summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_software_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_status_details
  # System Status Details
  # Get systems status detail dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_system_status_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_user_system_assignments_details
  # User System Assignments Details
  # Get user system assignments details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_user_system_assignments_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_omb_fsma_saop_summary
  # VA OMB FISMA SAOP Summary
  # Get VA OMB-FISMA SAOP summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_omb_fsma_saop_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_a2_summary
  # VA System A2.0 Summary
  # Get VA system A2.0 summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_a2_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_aa_summary
  # VA System A&amp;A Summary
  # Get VA system A&amp;A summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_aa_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_fisma_invetory_crypto_summary
  # VA System FISMA Inventory Crypto Summary
  # Get VA system FISMA inventory crypto summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_fisma_invetory_crypto_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_fisma_invetory_summary
  # VA System FISMA Inventory Summary
  # Get VA system FISMA inventory summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_fisma_invetory_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_pl109_reporting_summary
  # VA System P.L. 109 Reporting Summary
  # Get VA system P.L. 109 reporting summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_pl109_reporting_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_threat_architecture_details
  # VA System Threat Architecture Details
  # Get VA system threat architecture details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_threat_architecture_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_threat_risk_summary
  # VA System Threat Risks Summary
  # Get VA system threat risk summary dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_threat_risk_summary test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_va_system_threat_source_details
  # VA System Threat Sources Details
  # Get VA system threat source details dashboard information.
  # @param org_id **Organization Id**: The unique organization identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :excludeinherited **Exclude Inherited**: If no value is specified, the default returns false to include inherited data. 
  # @option opts [Integer] :page_index **Page Index**: If no value is specified, the default returns results from the first page with an index of 0. 
  # @option opts [Integer] :page_size **Page Size**: If no value is specified, the default returns 20000 per page. 
  # @return [Object]
  describe 'get_va_system_threat_source_details test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

end