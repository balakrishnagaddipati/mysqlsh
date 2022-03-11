# To Get DB Size
# USAGE 1 : \show locks
# USAGE 2 : \show locks -l 3
# The function definition is given as follows - show_dbsize (  3 arguments )

def expired_users(session, args, options):
  query = "SELECT concat(User, '@',Host) as User,password_expired as Expired,password_last_changed as Changed,password_lifetime as Lifetime,account_locked as Locked FROM mysql.user where password_expired='Y'"
  if (options.has_key('limit')):
    query += ' limit ' + str(options['limit'])

  result = session.run_sql(query);


  report = []
  if (result.has_data()):
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

  return {"report": report}


def locked_users(session, args, options):
  query = "SELECT concat(User, '@',Host) as User,password_expired as Expired,password_last_changed as Changed,password_lifetime as Lifetime,account_locked as Locked FROM mysql.user where account_locked='Y'"
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
def users_info(session, args, options):
  query = "SELECT concat(User, '@',Host) as User,password_expired as Expired,password_last_changed as Changed,password_lifetime as Lifetime,account_locked as Locked FROM mysql.user"
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

def users8_info(session, args, options):
  query = "SELECT concat(User, '@',Host) as User,password_expired as Expired,password_last_changed as Changed,password_lifetime as Lifetime,account_locked as Locked,User_attributes FROM mysql.user"
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
 
# Register the expired_users function as a MySQL Shell report
shell.register_report("expusers", "list", expired_users,
        {
        "brief":"List of Expired users.",
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

# Register the locked_users function as a MySQL Shell report
shell.register_report("lockedusers", "list", locked_users,
        {
        "brief":"List of Locked users.",
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


# Register the users_info function as a MySQL Shell report
shell.register_report("users", "list", users_info,
        {
        "brief":"Show List of users.",
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


# Register the users_info function as a MySQL Shell report
shell.register_report("users8", "list", users8_info,
        {
        "brief":"Show List of users.",
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