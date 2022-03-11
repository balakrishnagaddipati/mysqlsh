# To Get DB Size
# USAGE 1 : \show locks
# USAGE 2 : \show locks -l 3
# The function definition is given as follows - show_dbsize (  3 arguments )

def locks_info(session, args, options):
  query = "SELECT ENGINE_TRANSACTION_ID AS 'TranID', THREAD_ID, CONCAT(OBJECT_SCHEMA,'.',OBJECT_NAME) AS 'Table',LOCK_TYPE,LOCK_MODE,LOCK_STATUS,LOCK_DATA  FROM performance_schema.data_locks"
  if (options.has_key('limit')):
    query += ' limit ' + str(options['limit'])

  result = session.run_sql(query);


  report = []
  if (result.has_data()):
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

  return {"report": report}

### -----------------------------------------------------------
##def users_info(session, args, options):
##  query = "SELECT concat(User, '@',Host) as User,password_expired as Expired,password_last_changed as Changed,password_lifetime as Lifetime,account_locked as Locked,User_attributes FROM mysql.user"
##  if (options.has_key('limit')):
##    query += ' limit ' + str(options['limit'])
##
##  result = session.run_sql(query);
##
##
##  report = []
##  if (result.has_data()):
##    report = [result.get_column_names()]
##    for row in result.fetch_all():
##        report.append(list(row))
##
##  return {"report": report}
### -----------------------------------------------------------  
  
# Register the show_dbsize function as a MySQL Shell report
shell.register_report("locks", "list", locks_info,
        {
        "brief":"Show Locks.",
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


### Register the show_dbsize function as a MySQL Shell report
##shell.register_report("users", "list", users_info,
##        {
##        "brief":"Show Locks.",
##        'details': ['You need the SELECT privilege on sys.session view and the underlying tables and functions used by it.'],
##        'options': [
##            {
##                'name': 'limit',
##                'brief': 'The maximum number of rows to return.',
##                'shortcut': 'l',
##                'type': 'integer'
##            }
##        ],
##        'argc': '0'
##    }
##)