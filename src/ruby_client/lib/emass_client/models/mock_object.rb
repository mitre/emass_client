=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` POST endpoint to register the client certificate. The endpoint returns the user `api-key`. BOHA</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.12
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 7.1.0-SNAPSHOT

=end

require 'date'
require 'time'

module EmassClient
  class MockObject
    # [Required] Organization/Office represented. 100 Characters.
    attr_accessor :poc_organization

    # [Required] List of resources used. 250 Characters.
    attr_accessor :resources

    # [Read-Only] Owning organization of the system record. Values match the eMASS instance Organizational Hierarchy.
    attr_accessor :owning_organization

    # [Read-only] Secondary organization that owns the system record (i.e. Sub-Organization-level.
    attr_accessor :secondary_organization

    # [Conditional] First name of POC. 100 Characters.
    attr_accessor :poc_first_name

    # [Conditional] Last name of POC. 100 Characters.
    attr_accessor :poc_last_name

    # [Conditional] Email address of POC. 100 Characters.
    attr_accessor :poc_email

    # [Conditional] Phone number of POC (area code) ***-**** format. 100 Characters.
    attr_accessor :poc_phone_number

    # [Conditional] Required for approved items. Values include the following options: (Very Low, Low, Moderate,High,Very High)
    attr_accessor :severity

    # [Conditional] Required for ongoing and completed POA&M items. Unix time format.
    attr_accessor :scheduled_completion_date

    # [Conditional] Field is required for completed POA&M items. Unix time format.
    attr_accessor :completion_date

    # [Conditional] Field is required for completed and risk accepted POA&M items. 2000 Characters
    attr_accessor :comments

    # [Conditional] Optionally used in PUT to delete milestones when updating a POA&M.
    attr_accessor :is_active

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'poc_organization' => :'pocOrganization',
        :'resources' => :'resources',
        :'owning_organization' => :'owningOrganization',
        :'secondary_organization' => :'secondaryOrganization',
        :'poc_first_name' => :'pocFirstName',
        :'poc_last_name' => :'pocLastName',
        :'poc_email' => :'pocEmail',
        :'poc_phone_number' => :'pocPhoneNumber',
        :'severity' => :'severity',
        :'scheduled_completion_date' => :'scheduledCompletionDate',
        :'completion_date' => :'completionDate',
        :'comments' => :'comments',
        :'is_active' => :'isActive'
      }
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'poc_organization' => :'String',
        :'resources' => :'String',
        :'owning_organization' => :'String',
        :'secondary_organization' => :'String',
        :'poc_first_name' => :'String',
        :'poc_last_name' => :'String',
        :'poc_email' => :'String',
        :'poc_phone_number' => :'String',
        :'severity' => :'String',
        :'scheduled_completion_date' => :'Integer',
        :'completion_date' => :'Integer',
        :'comments' => :'String',
        :'is_active' => :'Boolean'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
        :'owning_organization',
        :'secondary_organization',
        :'scheduled_completion_date',
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `EmassClient::MockObject` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `EmassClient::MockObject`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'poc_organization')
        self.poc_organization = attributes[:'poc_organization']
      end

      if attributes.key?(:'resources')
        self.resources = attributes[:'resources']
      end

      if attributes.key?(:'owning_organization')
        self.owning_organization = attributes[:'owning_organization']
      end

      if attributes.key?(:'secondary_organization')
        self.secondary_organization = attributes[:'secondary_organization']
      end

      if attributes.key?(:'poc_first_name')
        self.poc_first_name = attributes[:'poc_first_name']
      end

      if attributes.key?(:'poc_last_name')
        self.poc_last_name = attributes[:'poc_last_name']
      end

      if attributes.key?(:'poc_email')
        self.poc_email = attributes[:'poc_email']
      end

      if attributes.key?(:'poc_phone_number')
        self.poc_phone_number = attributes[:'poc_phone_number']
      end

      if attributes.key?(:'severity')
        self.severity = attributes[:'severity']
      end

      if attributes.key?(:'scheduled_completion_date')
        self.scheduled_completion_date = attributes[:'scheduled_completion_date']
      end

      if attributes.key?(:'completion_date')
        self.completion_date = attributes[:'completion_date']
      end

      if attributes.key?(:'comments')
        self.comments = attributes[:'comments']
      end

      if attributes.key?(:'is_active')
        self.is_active = attributes[:'is_active']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      warn '[DEPRECATED] the `list_invalid_properties` method is obsolete'
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      warn '[DEPRECATED] the `valid?` method is obsolete'
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          poc_organization == o.poc_organization &&
          resources == o.resources &&
          owning_organization == o.owning_organization &&
          secondary_organization == o.secondary_organization &&
          poc_first_name == o.poc_first_name &&
          poc_last_name == o.poc_last_name &&
          poc_email == o.poc_email &&
          poc_phone_number == o.poc_phone_number &&
          severity == o.severity &&
          scheduled_completion_date == o.scheduled_completion_date &&
          completion_date == o.completion_date &&
          comments == o.comments &&
          is_active == o.is_active
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [poc_organization, resources, owning_organization, secondary_organization, poc_first_name, poc_last_name, poc_email, poc_phone_number, severity, scheduled_completion_date, completion_date, comments, is_active].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      attributes = attributes.transform_keys(&:to_sym)
      transformed_hash = {}
      openapi_types.each_pair do |key, type|
        if attributes.key?(attribute_map[key]) && attributes[attribute_map[key]].nil?
          transformed_hash["#{key}"] = nil
        elsif type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[attribute_map[key]].is_a?(Array)
            transformed_hash["#{key}"] = attributes[attribute_map[key]].map { |v| _deserialize($1, v) }
          end
        elsif !attributes[attribute_map[key]].nil?
          transformed_hash["#{key}"] = _deserialize(type, attributes[attribute_map[key]])
        end
      end
      new(transformed_hash)
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def self._deserialize(type, value)
      case type.to_sym
      when :Time
        Time.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        # models (e.g. Pet) or oneOf
        klass = EmassClient.const_get(type)
        klass.respond_to?(:openapi_one_of) ? klass.build(value) : klass.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end

        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end

  end

end