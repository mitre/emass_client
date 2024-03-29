=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The Enterprise Mission Assurance Support Service (eMASS) Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.   <strong>Register External Application (that use the eMASS API)</strong></br> New users will need to [register](https://nisp.emass.apps.mil/Content/Help/jobaids/eMASS_OT_NewUser_Job_Aid.pdf) an API key with the eMASS development team prior to accessing the site for the first time. The eMASS REST API  requires a client certificate (SSL/TLS, DoD PKI only). Use the `Registration` POST endpoint to register the client certificate. The endpoint call returns the user `api-key`.</br></br>  Every call to the eMASS REST API will require the use of the agreed upon public key certificate and API key.  The API key must be provided in the request header for all endpoint calls (api-key). If the service receives an untrusted certificate or API key, a 401 error response code will be returned along with an error message.</br></br>  <strong>Available Request Headers</strong></br> <table>   <tr>     <th align=left>key</th>     <th align=left>Example Value</th>     <th align=left>Description</th>   </tr>   <tr>     <td>`api-key`</td>     <td>api-key-provided-by-emass</td>     <td>This API key must be provided in the request header for all endpoint calls</td>   </tr>   <tr>     <td>`user-uid`</td>     <td>USER.UID.KEY</td>     <td>This User unique identifier key must be provided in the request header for all PUT, POST, and DELETE endpoint calls</td>   </tr>   <tr>     <td></td><td></td>     <td>       Note: For DoD users this is the DoD ID Number (EIDIPI) on their DoD CAC     </td>   </tr> </table>  </br><strong>Approve API Client for Actionable Requests</strong></br> Users are required to log-in to eMASS and grant permissions for a client to update data within eMASS on their behalf. This is only required for actionable requests (PUT, POST, DELETE). The Registration Endpoint and all GET requests can be accessed without completing this process with the correct permissions. Please note that leaving a field parameter blank (for PUT/POST requests) has the potential to clear information in the active eMASS records.  To establish an account with eMASS and/or acquire an api-key/user-uid, contact one of the listed POC: 

The version of the OpenAPI document: v3.12
Contact: disa.meade.id.mbx.emass-tier-iii-support@mail.mil
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 7.1.0-SNAPSHOT

=end

require 'cgi'

module EmassClient
  class ControlsApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Get control information in a system for one or many controls
    # Returns system control information for matching `systemId` path parameter
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :acronyms **Acronym**: The system acronym(s) being queried (single value or comma delimited values). (default to 'PM-6')
    # @return [ControlsResponseGet]
    def get_system_controls(system_id, opts = {})
      data, _status_code, _headers = get_system_controls_with_http_info(system_id, opts)
      data
    end

    # Get control information in a system for one or many controls
    # Returns system control information for matching &#x60;systemId&#x60; path parameter
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :acronyms **Acronym**: The system acronym(s) being queried (single value or comma delimited values). (default to 'PM-6')
    # @return [Array<(ControlsResponseGet, Integer, Hash)>] ControlsResponseGet data, response status code and response headers
    def get_system_controls_with_http_info(system_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: ControlsApi.get_system_controls ...'
      end
      # verify the required parameter 'system_id' is set
      if @api_client.config.client_side_validation && system_id.nil?
        fail ArgumentError, "Missing the required parameter 'system_id' when calling ControlsApi.get_system_controls"
      end
      # resource path
      local_var_path = '/api/systems/{systemId}/controls'.sub('{' + 'systemId' + '}', CGI.escape(system_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'acronyms'] = opts[:'acronyms'] if !opts[:'acronyms'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'ControlsResponseGet'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['apiKey', 'mockType', 'userId']

      new_options = opts.merge(
        :operation => :"ControlsApi.get_system_controls",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: ControlsApi#get_system_controls\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Update control information in a system for one or many controls
    #  Update a Control for given `systemId`<br>  **Request Body Required Fields** - `acronym` - `responsibleEntities` - `controlDesignation` - `estimatedCompletionDate` - `implementationNarrative`  The following optional fields (plus the **Request Body Required Fields**) are required based on the Implementation Status `implementationStatus` value<br> | Value                    | Required Fields |--------------------------|--------------------------------------------------- | Planned  or Implemented  | `slcmCriticality`, `slcmFrequency`, `slcmMethod`, `slcmReporting`, `slcmTracking`, `slcmComments` | Not Applicable           | `naJustification` | Manually Inherited       | `commonControlProvider`, `slcmCriticality`, `slcmFrequency`, `slcmMethod`, `slcmReporting`, `slcmTracking`, `slcmComments`  If the Implementation Status `implementationStatus` value is `Inherited`, only the following fields can be updated:   - `controlDesignation`   - `commonnControlProvider`  **NOTES:** - Implementation Plan information cannot be saved if the these fields exceed 2,000 character limits:   - `naJustification`,`responsibleEntities`,`implementationNarrative`,`slcmCriticality`   - `slcmFrequency`,`slcmMethod`,`slcmReporting`,`slcmTracking`,`slcmComments` - Implementation Plan information cannot be updated if Security Control does not exist in the system record.
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param request_body [Array<Object>] Update an existing control by Id
    # @param [Hash] opts the optional parameters
    # @return [ControlsResponsePut]
    def update_control_by_system_id(system_id, request_body, opts = {})
      data, _status_code, _headers = update_control_by_system_id_with_http_info(system_id, request_body, opts)
      data
    end

    # Update control information in a system for one or many controls
    #  Update a Control for given &#x60;systemId&#x60;&lt;br&gt;  **Request Body Required Fields** - &#x60;acronym&#x60; - &#x60;responsibleEntities&#x60; - &#x60;controlDesignation&#x60; - &#x60;estimatedCompletionDate&#x60; - &#x60;implementationNarrative&#x60;  The following optional fields (plus the **Request Body Required Fields**) are required based on the Implementation Status &#x60;implementationStatus&#x60; value&lt;br&gt; | Value                    | Required Fields |--------------------------|--------------------------------------------------- | Planned  or Implemented  | &#x60;slcmCriticality&#x60;, &#x60;slcmFrequency&#x60;, &#x60;slcmMethod&#x60;, &#x60;slcmReporting&#x60;, &#x60;slcmTracking&#x60;, &#x60;slcmComments&#x60; | Not Applicable           | &#x60;naJustification&#x60; | Manually Inherited       | &#x60;commonControlProvider&#x60;, &#x60;slcmCriticality&#x60;, &#x60;slcmFrequency&#x60;, &#x60;slcmMethod&#x60;, &#x60;slcmReporting&#x60;, &#x60;slcmTracking&#x60;, &#x60;slcmComments&#x60;  If the Implementation Status &#x60;implementationStatus&#x60; value is &#x60;Inherited&#x60;, only the following fields can be updated:   - &#x60;controlDesignation&#x60;   - &#x60;commonnControlProvider&#x60;  **NOTES:** - Implementation Plan information cannot be saved if the these fields exceed 2,000 character limits:   - &#x60;naJustification&#x60;,&#x60;responsibleEntities&#x60;,&#x60;implementationNarrative&#x60;,&#x60;slcmCriticality&#x60;   - &#x60;slcmFrequency&#x60;,&#x60;slcmMethod&#x60;,&#x60;slcmReporting&#x60;,&#x60;slcmTracking&#x60;,&#x60;slcmComments&#x60; - Implementation Plan information cannot be updated if Security Control does not exist in the system record.
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param request_body [Array<Object>] Update an existing control by Id
    # @param [Hash] opts the optional parameters
    # @return [Array<(ControlsResponsePut, Integer, Hash)>] ControlsResponsePut data, response status code and response headers
    def update_control_by_system_id_with_http_info(system_id, request_body, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: ControlsApi.update_control_by_system_id ...'
      end
      # verify the required parameter 'system_id' is set
      if @api_client.config.client_side_validation && system_id.nil?
        fail ArgumentError, "Missing the required parameter 'system_id' when calling ControlsApi.update_control_by_system_id"
      end
      # verify the required parameter 'request_body' is set
      if @api_client.config.client_side_validation && request_body.nil?
        fail ArgumentError, "Missing the required parameter 'request_body' when calling ControlsApi.update_control_by_system_id"
      end
      # resource path
      local_var_path = '/api/systems/{systemId}/controls'.sub('{' + 'systemId' + '}', CGI.escape(system_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      content_type = @api_client.select_header_content_type(['application/json'])
      if !content_type.nil?
          header_params['Content-Type'] = content_type
      end

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(request_body)

      # return_type
      return_type = opts[:debug_return_type] || 'ControlsResponsePut'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['apiKey', 'mockType', 'userId']

      new_options = opts.merge(
        :operation => :"ControlsApi.update_control_by_system_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:PUT, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: ControlsApi#update_control_by_system_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
