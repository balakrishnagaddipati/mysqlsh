# To Get DB Size
# USAGE : \show uptime

def up_time(session, args, options):
  query = "SELECT TIME_FORMAT(SEC_TO_TIME(VARIABLE_VALUE), '%Hh %im %ss') AS Uptime FROM performance_schema.global_status where VARIABLE_NAME='Uptime'"
  if (options.has_key('limit')):
    query += ' limit ' + str(options['limit'])
  result = session.run_sql(query);

  report = []
  if (result.has_data()):
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

  return {"report": report}
# -----------------------------------------------------------  

# Register the up_time function as a MySQL Shell report
shell.register_report("uptime", "list", up_time,
        {
        "brief":"Show server Uptime.",
        'details': ['You need the SELECT privilege on performance_schema.*'],
        'options': [
            {
                'name': 'limit',
                'brief': 'The maximum number of rows to return.',
                'shortcut': 'l',
                'type': 'integer'
            }
        ],
        'argc': '0'
    }
)


