dc_xml = """
<dublin_core>
{% if dc_creator %}<dcvalue element='creator' qualifier='none'>{{ dc_creator }}</dcvalue>{% endif %}
{% if dc_contributor_advisor %}<dcvalue element='contributor' qualifier='advisor'>{{ dc_contributor_advisor }}</dcvalue>{% endif %}
{% if dc_contributor_committeeMember %}{% for item in dc_contributor_committeeMember %}
  <dcvalue element='contributor' qualifier='committeeMember'>{{ item }}</dcvalue>
{%endfor %}{% endif %}
{% if dc_identifier %}<dcvalue element='identifier' qualifier='none'>{{ dc_identifier }}</dcvalue>{% endif %}
{% if dc_title %}<dcvalue element='title' qualifier='none'>{{ dc_title }}</dcvalue>{% endif %}
{% if dc_subject %}{% for item in dc_subject %}
  <dcvalue element='subject' qualifier='none'>{{ item }}</dcvalue>
{%endfor %}{% endif %}
{% if dc_subject_lsch %}<dcvalue element='subject' qualifier='lcsh'>{{ dc_subject_lsch }}</dcvalue>{% endif %}
{% if dc_subject_lsch_1 %}<dcvalue element='subject' qualifier='lcsh'>{{ dc_subject_lsch_1 }}</dcvalue>{% endif %}
{% if dc_description %}<dcvalue element='description' qualifier='none'>{{ dc_description }}</dcvalue>{% endif %}
{% if dc_description_abstract %}{% for item in dc_description_abstract %}
  <dcvalue element='description' qualifier='abstract'>{{ item }}</dcvalue>
{% endfor %}{% endif %}
{% if dc_date_issued %}<dcvalue element='date' qualifier='issued'>{{ dc_date_issued }}</dcvalue>{% endif %}
{% if dc_publisher %}<dcvalue element='publisher' qualifier='none'>{{ dc_publisher }}</dcvalue>{% endif %}
{% if dc_language %}<dcvalue element='language' qualifier='none'>{{ dc_language }}</dcvalue>{% endif %}
{% if dc_format %}<dcvalue element='format' qualifier='none'>{{ dc_format }}</dcvalue>{% endif %}
{% if dc_format_extent %}<dcvalue element='format' qualifier='extent'>{{ dc_format_extent }}</dcvalue>{% endif %}
{% if dc_format_medium %}<dcvalue element='format' qualifier='medium'>{{ dc_format_medium }}</dcvalue>{% endif %}
{% if dc_type %}{% for item in dc_type %}
  <dcvalue element='type' qualifier='none'>{{ item }}</dcvalue>
{% endfor %}{% endif %}
{% if dc_relation_requires %}<dcvalue element='relation' qualifier='requires'>{{ dc_relation_requires }}</dcvalue>{% endif %}
{% if dc_relation_uri %}<dcvalue element='relation' qualifier='uri'>{{ dc_relation_uri }}</dcvalue>{% endif %}
{% if dc_rights_uri %}<dcvalue element='rights' qualifier='uri'>{{ dc_rights_uri }}</dcvalue>{% endif %}
{% if dc_thesis_degree %}<dcvalue element='thesis' qualifier='degree'>{{ dc_thesis_degree }}</dcvalue>{% endif %}
</dublin_core>
"""

ou_xml = """
<dublin_core schema="ou">
{% if ou_group %}<dcvalue element='group' qualifier='none'>{{ ou_group }}</dcvalue>{% endif %}
</dublin_core>
"""