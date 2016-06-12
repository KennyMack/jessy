from core.database.sql import sql_text
from core.database.sql.conditions import Condition, Operation

class Command(object):
    """docstring for command"""
    def __init__(self, connection):
        self.connection = connection
        self.sql_command = ''
        self.last_id = -1

    def select(self, fields, table, **kwargs):
        self.connection.connect()
        self.cursor = self.connection.db.cursor()

        self.sql_command = sql_text.get_select_sql(
            sql_text.get_columns(fields), table, **kwargs)

        if kwargs.get('params'):
            self.cursor.execute(self.sql_command,
                                kwargs.get('params'))
        else:
            self.cursor.execute(self.sql_command)

        return self


    def insert(self, fields, table, **kwargs):
        self.last_id = -1
        if kwargs.get('params'):
            self.connection.connect()
            self.cursor = self.connection.db.cursor()

            self.sql_command = sql_text.get_insert_sql(
                sql_text.get_columns(fields), table)


            self.cursor.execute(self.sql_command,
                                kwargs.get('params'))

            self.last_id = self.cursor.lastrowid

            if kwargs.get('auto_commit', True):
                self.connection.commit()
                self.connection.close()

        return self


    def all(self):
        if self.cursor:
            rows = []
            for row in self.cursor.fetchall():
                rows.append(row)

            self.connection.close()
            return rows

        return []


    def first(self):
        if self.cursor:
            ret = self.cursor.fetchone()
            self.connection.close()
            return ret
        print('fim')


#a = Command('')
#
#a.insert(('col1', 'col2',), 'jessy')
#
#a.select((sql_text.table_column('dummy', 'col1'),'col2','col4','col3'),
#         'dummy',
#         join=(
#            sql_text.table_join(
#                { 'dummy': ('col1', ) },
#                { 'tblow': ('col1', ) }
#            )
#         ),
#         condition=(
#             sql_text.add_condition(
#                ((Condition.AND, 'dummy', 'col1', Operation.EQUAL),
#                (Condition.AND, 'dummy', 'col1', Operation.EQUAL))
#            )
#         )
#         ).conn()
#
