# To Get Cluster Status
# USAGE 1 : \show locks
# USAGE 2 : \show locks -l 3
# The function definition is given as follows - show_dbsize (  3 arguments )

def cluster_status(session, args, options):
  query = "select MEMBER_HOST,MEMBER_PORT,MEMBER_STATE,MEMBER_ROLE,MEMBER_VERSION from performance_schema.replication_group_members"
  if (options.has_key('limit')):
    query += ' limit ' + str(options['limit'])

  result = session.run_sql(query);


  report = []
  if (result.has_data()):
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

  return {"report": report}

# Register the cluster_status function as a MySQL Shell report
shell.register_report("clusstatus", "list", cluster_status,
        {
        "brief":"Display Cluster Status.",
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
