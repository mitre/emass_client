=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The eMASS Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.  The eMASS API provides an interface for application to communicate eMASS Services. For information on how to register and use the eMASS API reference the [eMASS API Getting Started](eMASSGettingStarted.md).  Additional information about eMASS can be obtain by contacting the National Industrial Security Program (NISP). Points of Contact are: 

The version of the OpenAPI document: v3.22
Contact: disa.global.servicedesk.mbx.ma-ticket-request@mail.mil
Generated by: https://openapi-generator.tech
Generator version: 7.12.0-SNAPSHOT

=end

require 'spec_helper'
require 'json'

# Unit tests for EmassClient::CACApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'CACApi' do
  before do
    # run before each test
    @api_instance = EmassClient::CACApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of CACApi' do
    it 'should create an instance of CACApi' do
      expect(@api_instance).to be_instance_of(EmassClient::CACApi)
    end
  end

  # unit tests for add_system_cac
  # Submit control to second role of CAC
  # **Request Body Required Fields** - &#x60;controlAcronym&#x60; - &#x60;comments&#x60;  **NOTES:** - Comments &#x60;comments&#x60; are not required at the first role of the CAC but are required at the second role of the CAC. Comments cannot exceed 10,000 characters. - POST requests will only yield successful results if the control is currently sitting at the first role of the CAC. If the control is not currently sitting at the first role, then an error will be returned.
  # @param system_id **System Id**: The unique system record identifier.
  # @param request_body Example request body for adding control(s) to second role of CAC
  # @param [Hash] opts the optional parameters
  # @return [CacResponsePost]
  describe 'add_system_cac test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_cac
  # Get location of one or many controls in CAC
  # Returns the location of a system&#39;s package in the Control Approval Chain (CAC) for matching &#x60;systemId&#x60; path parameter
  # @param system_id **System Id**: The unique system record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :control_acronyms **Control Acronym**: Filter query by given system acronym (single value or comma separated).
  # @return [CacResponseGet]
  describe 'get_system_cac test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

end
