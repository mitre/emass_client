=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The eMASS Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.  The eMASS API provides an interface for application to communicate eMASS Services. For information on how to register and use the eMASS API reference the [eMASS API Getting Started](eMASSGettingStarted.md).  Additional information about eMASS can be obtain by contacting the National Industrial Security Program (NISP). Points of Contact are: 

The version of the OpenAPI document: v3.22
Contact: disa.global.servicedesk.mbx.ma-ticket-request@mail.mil
Generated by: https://openapi-generator.tech
Generator version: 7.12.0-SNAPSHOT

=end

require 'date'
require 'time'

module EmassClient
  class PoamReadOnlyFields
    # [Read-Only] Unique identifier of the authorization term/condition linked to the POA&M Item.
    attr_accessor :condition_id

    # [Read-only] Indicates whether a test result is inherited.
    attr_accessor :is_inherited

    # [Read-Only] CCI associated with POA&M Item.
    attr_accessor :cci

    # [Read-Only] Values include the following options: (Not Approved,Under Review,Approved)
    attr_accessor :review_status

    # [Read-Only] Timestamp representing when the POA&M Item was entered into the database.
    attr_accessor :created_date

    # [Read-Only] Value returned for a POA&M Item with review status \"Approved\" and has a milestone with a scheduled completion date that extends beyond the POA&M Item's scheduled completion date. 
    attr_accessor :extension_date

    # [Read-Only] Value returned for a POA&M Item with a review status of \"Approved\" and an unapproved milestone with a scheduled completion date that extends beyond the POA&M Item's scheduled completion date. 
    attr_accessor :pending_extension_date

    # [Read-Only] Lists the filenames of any artifact files attached to the POA&M Item. Multiple values are separated by “; ”.
    attr_accessor :artifacts

    class EnumAttributeValidator
      attr_reader :datatype
      attr_reader :allowable_values

      def initialize(datatype, allowable_values)
        @allowable_values = allowable_values.map do |value|
          case datatype.to_s
          when /Integer/i
            value.to_i
          when /Float/i
            value.to_f
          else
            value
          end
        end
      end

      def valid?(value)
        !value || allowable_values.include?(value)
      end
    end

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'condition_id' => :'conditionId',
        :'is_inherited' => :'isInherited',
        :'cci' => :'cci',
        :'review_status' => :'reviewStatus',
        :'created_date' => :'createdDate',
        :'extension_date' => :'extensionDate',
        :'pending_extension_date' => :'pendingExtensionDate',
        :'artifacts' => :'artifacts'
      }
    end

    # Returns attribute mapping this model knows about
    def self.acceptable_attribute_map
      attribute_map
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      acceptable_attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'condition_id' => :'String',
        :'is_inherited' => :'Boolean',
        :'cci' => :'String',
        :'review_status' => :'String',
        :'created_date' => :'Integer',
        :'extension_date' => :'Integer',
        :'pending_extension_date' => :'Integer',
        :'artifacts' => :'String'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
        :'condition_id',
        :'is_inherited',
        :'cci',
        :'review_status',
        :'extension_date',
        :'pending_extension_date',
        :'artifacts'
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `EmassClient::PoamReadOnlyFields` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      acceptable_attribute_map = self.class.acceptable_attribute_map
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!acceptable_attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `EmassClient::PoamReadOnlyFields`. Please check the name to make sure it's valid. List of attributes: " + acceptable_attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'condition_id')
        self.condition_id = attributes[:'condition_id']
      end

      if attributes.key?(:'is_inherited')
        self.is_inherited = attributes[:'is_inherited']
      end

      if attributes.key?(:'cci')
        self.cci = attributes[:'cci']
      end

      if attributes.key?(:'review_status')
        self.review_status = attributes[:'review_status']
      end

      if attributes.key?(:'created_date')
        self.created_date = attributes[:'created_date']
      end

      if attributes.key?(:'extension_date')
        self.extension_date = attributes[:'extension_date']
      end

      if attributes.key?(:'pending_extension_date')
        self.pending_extension_date = attributes[:'pending_extension_date']
      end

      if attributes.key?(:'artifacts')
        self.artifacts = attributes[:'artifacts']
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
      review_status_validator = EnumAttributeValidator.new('String', ["Not Approved", "Under Review", "Approved", "unknown_default_open_api"])
      return false unless review_status_validator.valid?(@review_status)
      true
    end

    # Custom attribute writer method checking allowed values (enum).
    # @param [Object] review_status Object to be assigned
    def review_status=(review_status)
      validator = EnumAttributeValidator.new('String', ["Not Approved", "Under Review", "Approved", "unknown_default_open_api"])
      unless validator.valid?(review_status)
        fail ArgumentError, "invalid value for \"review_status\", must be one of #{validator.allowable_values}."
      end
      @review_status = review_status
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          condition_id == o.condition_id &&
          is_inherited == o.is_inherited &&
          cci == o.cci &&
          review_status == o.review_status &&
          created_date == o.created_date &&
          extension_date == o.extension_date &&
          pending_extension_date == o.pending_extension_date &&
          artifacts == o.artifacts
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [condition_id, is_inherited, cci, review_status, created_date, extension_date, pending_extension_date, artifacts].hash
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
        klass.respond_to?(:openapi_any_of) || klass.respond_to?(:openapi_one_of) ? klass.build(value) : klass.build_from_hash(value)
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
