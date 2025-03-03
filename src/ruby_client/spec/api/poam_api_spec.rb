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

# Unit tests for EmassClient::POAMApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'POAMApi' do
  before do
    # run before each test
    @api_instance = EmassClient::POAMApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of POAMApi' do
    it 'should create an instance of POAMApi' do
      expect(@api_instance).to be_instance_of(EmassClient::POAMApi)
    end
  end

  # unit tests for add_poam_by_system_id
  # Add one or many POA&amp;M items in a system
  # Add a POA&amp;M for given &#x60;systemId&#x60;  **Request Body Required Fields** &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;&lt;th&gt;&lt;b&gt;Field&lt;/b&gt;&lt;/th&gt;&lt;th&gt;&lt;b&gt;Require/Condition&lt;/b&gt;&lt;/th&gt;&lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;status&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every POST)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;vulnerabilityDescription&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every POST)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;sourceIdentifyingVulnerability&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every POST)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocOrganization&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every POST)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;resources&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every POST)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;identifiedInCFOAuditOrOtherReview&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Required for VA. Optional for Army and USCG.&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;scheduledCompletionDate&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Required for ongoing and completed POA&amp;M items&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocFirstName&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if Last Name, Email, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocLastName&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Email, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocEmail&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Last Name, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocPhoneNumber&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Last Name, or Email have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;completionDate&lt;/code&gt;&lt;/td&gt;&lt;td&gt;For completed POA&amp;M Item only&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;comments&lt;/code&gt;&lt;/td&gt;&lt;td&gt;For completed or Risk Accepted POA&amp;M Items only&lt;/td&gt;&lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;  **NOTE**: Certain eMASS instances also require the Risk Analysis fields to be populated:   - &#x60;severity&#x60;   - &#x60;relevanceOfThreat&#x60;   - &#x60;likelihood&#x60;   - &#x60;impact&#x60;   - &#x60;residualRiskLevel&#x60;   - &#x60;mitigations&#x60;  &lt;/br&gt; **Business Rules**  The following rules apply to the Review Status &#x60;status&#x60; field value: &lt;table&gt;   &lt;thead&gt;&lt;tr&gt;&lt;th&gt;&lt;b&gt;Value&lt;/b&gt;&lt;/th&gt;&lt;th&gt;&lt;b&gt;Rule&lt;/b&gt;&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;&lt;td&gt;&lt;b&gt;Not Approved&lt;/b&gt;&lt;/td&gt;&lt;td&gt;POA&amp;M cannot be saved if Milestone Scheduled Completion Date exceeds POA&amp;M Item Scheduled Completion Date&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;b&gt;Approved&lt;/b&gt;&lt;/td&gt;&lt;td&gt;POA&amp;M can only be saved if Milestone Scheduled Completion Date exceeds POA&amp;M Item Scheduled Completion Date&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;Are required to have a Severity Value assigned&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;b&gt;Completed&lt;/b&gt; or &lt;b&gt;Ongoing&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Cannot be saved without Milestones&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;b&gt;Risk Accepted&lt;/b&gt;&lt;/td&gt;&lt;td&gt;POA&amp;M Item cannot be saved with a Scheduled Completion Date &lt;code&gt;scheduledCompletionDate&lt;/code&gt; or have Milestones&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;b&gt;Approved&lt;/b&gt; or &lt;b&gt;Completed&lt;/b&gt; or &lt;b&gt;Ongoing&lt;/b&gt;&lt;/td&gt;&lt;td&gt;Cannot update Scheduled Completion Date&lt;/td&gt;&lt;/tr&gt;  &lt;/tbody&gt; &lt;/table&gt;  **Additional Rules** - POA&amp;M Item cannot be saved if associated Security Control or AP is inherited. - Completed POA&amp;M Item cannot be saved if Completion Date (&#x60;completionDate&#x60;) is in the future. - POA&amp;M Items cannot be updated if they are included in an active package. - Archived POA&amp;M Items cannot be updated. - POA&amp;M Items with a status of \&quot;Not Applicable\&quot; will be updated through test result creation. - If the Security Control or Assessment Procedure does not exist in the system, the POA&amp;M Item maybe imported at the System Level.   **Fields Characters Limitation** - POA&amp;M Item cannot be saved if the Point of Contact (POC) fields exceed 100 characters:   - &#x60;pocOrganization&#x60; &#x60;pocFirstName&#x60;, &#x60;pocLastName&#x60;, &#x60;pocEmail&#x60;, &#x60;pocPhoneNumber&#x60; - POA&amp;M Item cannot be saved if Resources (&#x60;resource&#x60;) field exceeds 250 characters - POA&amp;M Item cannot be saved if the following fields exceeds 2,000 characters:   - &#x60;mitigations&#x60;, &#x60;sourceIdentifyingVulnerability&#x60;, &#x60;comments&#x60;   - Milestones Field: &#x60;description&#x60; - POA&amp;M Items cannot be saved if Milestone Description (&#x60;description&#x60;) exceeds 2,000 characters.
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_required_fields Example request body to add POA&amp;M(s) to a system (systemId)
  # @param [Hash] opts the optional parameters
  # @return [PoamResponsePostPutDelete]
  describe 'add_poam_by_system_id test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for delete_poam
  # Remove one or many POA&amp;M items in a system
  # Remove the POA&amp;M matching &#x60;systemId&#x60; path parameter and &#x60;poamId&#x60; Request Body&lt;br&gt;
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_request_delete_body_inner Delete the given POA&amp;M Id
  # @param [Hash] opts the optional parameters
  # @return [PoamResponsePostPutDelete]
  describe 'delete_poam test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_poams
  # Get one or many POA&amp;M items in a system
  # Returns system(s) containing POA&amp;M items for matching parameters.
  # @param system_id **System Id**: The unique system record identifier.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :scheduled_completion_date_start **Date Started**: Filter query by the scheduled completion start date (Unix date format).
  # @option opts [String] :scheduled_completion_date_end **Date Ended**: Filter query by the scheduled completion start date (Unix date format).
  # @option opts [String] :control_acronyms **Control Acronym**: Filter query by given system acronym (single value or comma separated).
  # @option opts [String] :assessment_procedures **Assessment Procedure**: Filter query by given Security Control Assessment Procedure (single value or comma separated).
  # @option opts [String] :ccis **CCI System**: Filter query by Control Correlation Identifiers (CCIs) (single value or comma separated).
  # @option opts [Boolean] :system_only **Systems Only**: Indicates that only system(s) information is retrieved.
  # @return [PoamResponseGetSystems]
  describe 'get_system_poams test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for get_system_poams_by_poam_id
  # Get POA&amp;M item by ID in a system
  # Returns system(s) containing POA&amp;M items for matching parameters.
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_id **POA&amp;M Id**: The unique POA&amp;M record identifier.
  # @param [Hash] opts the optional parameters
  # @return [PoamResponseGetPoams]
  describe 'get_system_poams_by_poam_id test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

  # unit tests for update_poam_by_system_id
  # Update one or many POA&amp;M items in a system
  # Update a POA&amp;M for given &#x60;systemId&#x60;&lt;br&gt;  **Request Body Required Fields** &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;&lt;th&gt;&lt;b&gt;Field&lt;/b&gt;&lt;/th&gt;&lt;th&gt;&lt;b&gt;Require/Condition&lt;/b&gt;&lt;/th&gt;&lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;poamId&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;displayPoamId&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;status&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;vulnerabilityDescription&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;sourceIdentifyingVulnerability&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocOrganization&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;resources&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Always (every PUT)&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;identifiedInCFOAuditOrOtherReview&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Required for VA. Optional for Army and USCG.&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;scheduledCompletionDate&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Required for ongoing and completed POA&amp;M items&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocFirstName&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if Last Name, Email, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocLastName&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Email, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocEmail&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Last Name, or Phone Number have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;pocPhoneNumber&lt;/code&gt;&lt;/td&gt;&lt;td&gt;Only if First Name, Last Name, or Email have data&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;completionDate&lt;/code&gt;&lt;/td&gt;&lt;td&gt;For completed POA&amp;M Item only&lt;/td&gt;&lt;/tr&gt;     &lt;tr&gt;&lt;td&gt;&lt;code&gt;comments&lt;/code&gt;&lt;/td&gt;&lt;td&gt;For completed or Risk Accepted POA&amp;M Items only&lt;/td&gt;&lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;  **NOTES**: - Certain eMASS instances also require the Risk Analysis fields to be populated:   - &#x60;severity&#x60;   - &#x60;relevanceOfThreat&#x60;   - &#x60;likelihood&#x60;   - &#x60;impact&#x60;   - &#x60;residualRiskLevel&#x60;   - &#x60;mitigations&#x60; - To prevent uploading duplicate/undesired milestones through the POA&amp;M PUT include an &#x60;isActive&#x60; field for the milestone and set it to equal to false &#x60;(isActive&#x3D;false)&#x60;. &lt;/br&gt;  **Business Rules:** See business rules for the POST endpoint
  # @param system_id **System Id**: The unique system record identifier.
  # @param poam_ids Example request body for updating a POA&amp;M for a system (systemId)
  # @param [Hash] opts the optional parameters
  # @return [PoamResponsePostPutDelete]
  describe 'update_poam_by_system_id test' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

end
