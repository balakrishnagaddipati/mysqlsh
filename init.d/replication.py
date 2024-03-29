# To find recovery process
# USAGE 1 : \show gr_recovery_progress
def gr_recovery_progress(session):
    result = session.run_sql("select substring_index(substring_index(GTID_SUBTRACT(RECEIVED_TRANSACTION_SET,@@gtid_executed),':',-1),'-',-1)-substring_index(substring_index(GTID_SUBTRACT(RECEIVED_TRANSACTION_SET,@@gtid_executed),':',-1),'-',1) as Trx_to_recover from performance_schema.replication_connection_status where channel_name='group_replication_recovery'")


    #result = query.execute()
    report = [result.get_column_names()]
    for row in result.fetch_all():
        report.append(list(row))

    return {'report': report}
# -----------------------------------------------------------  

# Register the gr_recovery_progress function as a MySQL Shell report
shell.register_report(
    'gr_recovery_progress',
    'list',
    gr_recovery_progress,
    {
        'brief': 'Shows Group Replication Async Recovery Progress on the joiner.',
        'details': ['You need the SELECT privilege on sys.session view and the '
                    + 'underlying tables and functions used by it.'],
        'argc': '0'
    }
)
