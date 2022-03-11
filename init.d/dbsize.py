# To Get DB Size
# USAGE 1 : \show locks
# USAGE 2 : \show locks -l 3
# The function definition is given as follows - show_dbsize (  3 arguments )

def show_dbsize(session, args, options):
  query = "SELECT ROUND(SUM(data_length + index_length) / 1024 / 1024 / 1024, 2) AS 'Size (GB)', count(table_schema) as '# of Schemas' FROM information_schema.TABLES"
  if (options.has_key('limit')):
    query += ' limit ' + str(options['limit'])

  result = session.run_sql(query);


  report = []
  if (result.has_data()):
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

  return {"report": report}


def show_schemasize(session, args, options):
  query = "SELECT table_schema AS 'Database', ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)', count(table_name) as '# of tables' FROM information_schema.TABLES GROUP BY table_schema order by 2 desc"
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
def show_tablesize(session, args, options):
  query = "SELECT table_schema AS 'Database',table_name, ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)' FROM information_schema.TABLES GROUP BY table_schema,table_name order by 3 desc"
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
  
# Register the show_dbsize function as a MySQL Shell report
shell.register_report("dbsize", "list", show_dbsize,
        {
        "brief":"Database Size.",
        'details': ['You need the SELECT privilege on sys.session view and the underlying tables and functions used by it.'],
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

# Register the show_schemasize function as a MySQL Shell report
shell.register_report("schemasize", "list", show_schemasize,
        {
        "brief":"Schemas Size",
        'details': ['You need the SELECT privilege on sys.session view and the underlying tables and functions used by it.'],
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


# Register the show_tablesize function as a MySQL Shell report
shell.register_report("tablesize", "list", show_tablesize,
        {
        "brief":"Tables Size",
        'details': ['You need the SELECT privilege on sys.session view and the underlying tables and functions used by it.'],
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