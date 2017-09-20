uint32 {{cookiecutter.app_name}}_{{cookiecutter.msg_name}}_Enc(const {{cookiecutter.msg_name}} *inObject, char *inOutBuffer, uint32 inSize)
{
	bool status = false;
	{{cookiecutter.pb_msg_type}} pbMsg;

	{% for pb_var, var_data in cookiecutter.pb_variables.iteritems() %}{% if var_data.array_len| int > 0 %}{% for i in range(0, var_data.array_len | int) %}
	{% if var_data.type == "string" %}strcpy(pbMsg.{{pb_var}}[{{loop.index0}}], inObject->{{var_data.air_name}}[{{loop.index0}}]);{% else %}pbMsg.{{pb_var}}[{{loop.index0}}] = inObject->{{var_data.air_name}}[{{loop.index0}}];
	{%- endif -%}
	{%- endfor -%}
	{%- else -%}
	{% if var_data.type == "string" %}strcpy(pbMsg.{{pb_var}}, inObject->{{var_data.air_name}});
	{% else %}pbMsg.{{pb_var}} = inObject->{{var_data.air_name}};
	{%- endif -%}
	{%- endif -%}
	{% endfor %}

	/* Create a stream that will write to our buffer. */
	pb_ostream_t stream = pb_ostream_from_buffer((pb_byte_t *)inOutBuffer, inSize);

	/* Now we are ready to encode the message. */
	status = pb_encode(&stream, {{cookiecutter.pb_msg_type}}_fields, &pbMsg); 
	/* Check for errors... */
	if (!status)
	{
		return 0;
	}

	return stream.bytes_written;
}

uint32 {{cookiecutter.app_name}}_{{cookiecutter.msg_name}}_Dec(const char *inBuffer, uint32 inSize, {{cookiecutter.msg_name}} *inOutObject)
{
	bool status = false;
	{{cookiecutter.pb_msg_type}} pbMsg;

	/* Create a stream that reads from the buffer. */
	pb_istream_t stream = pb_istream_from_buffer((const pb_byte_t *)inBuffer, inSize);

	/* Now we are ready to decode the message. */
	status = pb_decode(&stream, {{cookiecutter.pb_msg_type}}_fields, &pbMsg); 

	/* Check for errors... */
	if (!status)
	{
		return 0;
	}
	
	{% for pb_var, var_data in cookiecutter.pb_variables.iteritems() %}{% if var_data.array_len| int > 0 %}{% for i in range(0, var_data.array_len | int) %}
	{% if var_data.type == "string" %}strcpy(inOutObject->{{var_data.air_name}}[{{loop.index0}}], pbMsg.{{pb_var}}[{{loop.index0}}]);{% else %}inOutObject->{{var_data.air_name}}[{{loop.index0}}] = pbMsg.{{pb_var}}[{{loop.index0}}];
	{%- endif -%}
	{%- endfor -%}
	{%- else -%}
	{% if var_data.type == "string" %}strcpy(inOutObject->{{var_data.air_name}}, pbMsg.{{pb_var}});
	{% else %}inOutObject->{{var_data.air_name}} = pbMsg.{{pb_var}};
	{%- endif -%}
	{%- endif -%}
	{% endfor %}

	return sizeof({{cookiecutter.msg_name}});
}
