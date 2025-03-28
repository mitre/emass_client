=begin
#Enterprise Mission Assurance Support Service (eMASS)

#The eMASS Representational State Transfer (REST) Application Programming Interface (API) enables users to perform assessments and complete actions associated with system records.  The eMASS API provides an interface for application to communicate eMASS Services. For information on how to register and use the eMASS API reference the [eMASS API Getting Started](eMASSGettingStarted.md).  Additional information about eMASS can be obtain by contacting the National Industrial Security Program (NISP). Points of Contact are: 

The version of the OpenAPI document: v3.22
Contact: disa.global.servicedesk.mbx.ma-ticket-request@mail.mil
Generated by: https://openapi-generator.tech
Generator version: 7.12.0-SNAPSHOT

=end

require 'cgi'

module EmassClient
  class ContainerScanResultsApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Add one or many containers and their scan results
    # Add containers and their scan results in the assets module for a system `systemId`.  **Request Body Required Fields** - `containerId` - `containerName` - `time` - `benchmarks` (Object Array)   - `benchmark`   - `results` (Object Array)     - `ruleId`     - `status`     - `lastSeen`  **Example Request Body Required Fields** ``` [   {     \"containerId\": \"container identification\",     \"containerName\": \"container name\",     \"time\": Datetime of scan/result (1648217219),     \"benchmarks\": [       {         \"benchmark\": \"RHEL_8_STIG\",         \"results\": [           {             \"ruleId\": \"rule identification\",             \"status\": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \"lastSeen\": Unix date format (1648217219)           }, {             \"ruleId\": \"rule identification\",             \"status\": [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \"lastSeen\": Unix date format (1648217219)           }         ]       }     ]   } ] ````
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param request_body [Array<Object>] Example request body for adding containers and their scan results
    # @param [Hash] opts the optional parameters
    # @return [ContainersResponsePost]
    def add_container_sans_by_system_id(system_id, request_body, opts = {})
      data, _status_code, _headers = add_container_sans_by_system_id_with_http_info(system_id, request_body, opts)
      data
    end

    # Add one or many containers and their scan results
    # Add containers and their scan results in the assets module for a system &#x60;systemId&#x60;.  **Request Body Required Fields** - &#x60;containerId&#x60; - &#x60;containerName&#x60; - &#x60;time&#x60; - &#x60;benchmarks&#x60; (Object Array)   - &#x60;benchmark&#x60;   - &#x60;results&#x60; (Object Array)     - &#x60;ruleId&#x60;     - &#x60;status&#x60;     - &#x60;lastSeen&#x60;  **Example Request Body Required Fields** &#x60;&#x60;&#x60; [   {     \&quot;containerId\&quot;: \&quot;container identification\&quot;,     \&quot;containerName\&quot;: \&quot;container name\&quot;,     \&quot;time\&quot;: Datetime of scan/result (1648217219),     \&quot;benchmarks\&quot;: [       {         \&quot;benchmark\&quot;: \&quot;RHEL_8_STIG\&quot;,         \&quot;results\&quot;: [           {             \&quot;ruleId\&quot;: \&quot;rule identification\&quot;,             \&quot;status\&quot;: [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \&quot;lastSeen\&quot;: Unix date format (1648217219)           }, {             \&quot;ruleId\&quot;: \&quot;rule identification\&quot;,             \&quot;status\&quot;: [Pass,Fail,Other,Not Reviewed,Not Checked,Not Applicable],             \&quot;lastSeen\&quot;: Unix date format (1648217219)           }         ]       }     ]   } ] &#x60;&#x60;&#x60;&#x60;
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param request_body [Array<Object>] Example request body for adding containers and their scan results
    # @param [Hash] opts the optional parameters
    # @return [Array<(ContainersResponsePost, Integer, Hash)>] ContainersResponsePost data, response status code and response headers
    def add_container_sans_by_system_id_with_http_info(system_id, request_body, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: ContainerScanResultsApi.add_container_sans_by_system_id ...'
      end
      # verify the required parameter 'system_id' is set
      if @api_client.config.client_side_validation && system_id.nil?
        fail ArgumentError, "Missing the required parameter 'system_id' when calling ContainerScanResultsApi.add_container_sans_by_system_id"
      end
      # verify the required parameter 'request_body' is set
      if @api_client.config.client_side_validation && request_body.nil?
        fail ArgumentError, "Missing the required parameter 'request_body' when calling ContainerScanResultsApi.add_container_sans_by_system_id"
      end
      # resource path
      local_var_path = '/api/systems/{systemId}/container-scan-results'.sub('{' + 'systemId' + '}', CGI.escape(system_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json']) unless header_params['Accept']
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
      return_type = opts[:debug_return_type] || 'ContainersResponsePost'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['apiKey', 'mockType', 'userId']

      new_options = opts.merge(
        :operation => :"ContainerScanResultsApi.add_container_sans_by_system_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: ContainerScanResultsApi#add_container_sans_by_system_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Remove one or many containers in a system
    # Removes container scan resources and their scan results in the assets module for a system `systemId`
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param container_resources_delete_body_inner [Array<ContainerResourcesDeleteBodyInner>] Delete the given Container Scan Id
    # @param [Hash] opts the optional parameters
    # @return [ContainersResponseDelete]
    def delete_container_sans(system_id, container_resources_delete_body_inner, opts = {})
      data, _status_code, _headers = delete_container_sans_with_http_info(system_id, container_resources_delete_body_inner, opts)
      data
    end

    # Remove one or many containers in a system
    # Removes container scan resources and their scan results in the assets module for a system &#x60;systemId&#x60;
    # @param system_id [Integer] **System Id**: The unique system record identifier.
    # @param container_resources_delete_body_inner [Array<ContainerResourcesDeleteBodyInner>] Delete the given Container Scan Id
    # @param [Hash] opts the optional parameters
    # @return [Array<(ContainersResponseDelete, Integer, Hash)>] ContainersResponseDelete data, response status code and response headers
    def delete_container_sans_with_http_info(system_id, container_resources_delete_body_inner, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: ContainerScanResultsApi.delete_container_sans ...'
      end
      # verify the required parameter 'system_id' is set
      if @api_client.config.client_side_validation && system_id.nil?
        fail ArgumentError, "Missing the required parameter 'system_id' when calling ContainerScanResultsApi.delete_container_sans"
      end
      # verify the required parameter 'container_resources_delete_body_inner' is set
      if @api_client.config.client_side_validation && container_resources_delete_body_inner.nil?
        fail ArgumentError, "Missing the required parameter 'container_resources_delete_body_inner' when calling ContainerScanResultsApi.delete_container_sans"
      end
      # resource path
      local_var_path = '/api/systems/{systemId}/container-scan-results'.sub('{' + 'systemId' + '}', CGI.escape(system_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json']) unless header_params['Accept']
      # HTTP header 'Content-Type'
      content_type = @api_client.select_header_content_type(['application/json'])
      if !content_type.nil?
          header_params['Content-Type'] = content_type
      end

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(container_resources_delete_body_inner)

      # return_type
      return_type = opts[:debug_return_type] || 'ContainersResponseDelete'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['apiKey', 'mockType', 'userId']

      new_options = opts.merge(
        :operation => :"ContainerScanResultsApi.delete_container_sans",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: ContainerScanResultsApi#delete_container_sans\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
