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

# Unit tests for EmassClient::SystemRolesApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'SystemRolesApi' do
  before do
    # run before each test
    @api_instance = EmassClient::SystemRolesApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of SystemRolesApi' do
    it 'should create an instance of SystemRolesApi' do
      expect(@api_instance).to be_instance_of(EmassClient::SystemRolesApi)
    end
  end

  # unit tests for get_system_roles
  # Get available roles
  # Returns all available roles
  # @param [Hash] opts the optional parameters
  # @return [SystemRolesResponse]
  describe 'get_system_roles test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_roles_by_category_id
  # Get system roles
  # Returns the role(s) data matching parameters.
  # @param role_category **Role Category**: The system role category been queried
  # @param role **Role**: Accepts single value from options available at base system-roles endpoint e.g., SCA.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :policy **System Policy**: Filter query by system policy. If no value is specified, the default returns RMF policy information for dual-policy systems.
  # @return [SystemRolesCategoryResponse]
  describe 'get_system_roles_by_category_id test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

end
