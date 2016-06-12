from core.database.sql.conditions import Condition, Operation

def table_column(table, column):
    return "{0}.{1}".format(table, column)


def get_columns(columns):
    sql = []
    for r in columns:
        sql.append(r)

    return ", ".join(sql)


def get_insert_sql(columns, table):
    sql = []
    sql.append('insert into')
    sql.append(table)
    sql.append('(')
    sql.append(columns)
    sql.append(') values (')
    pars = []
    for i in columns.split(','):
        pars.append( '?' )
    sql.append(", ".join(pars))
    sql.append(')')
    return "\r\n".join(sql)


def get_update_sql(columns, table, **kwargs):
    sql = []
    sql.append('update')
    sql.append(table)
    sql.append('set')

    cols = []
    for col in columns:
        cols.append("{0} = ?".format(col))
    sql.append(",\r\n".join(cols))

    if kwargs.get('condition'):
        sql.append('where')
        sql.append(kwargs['condition'][3:])

    return "\r\n".join(sql)



def get_delete_sql(table, **kwargs):
    sql = []
    sql.append('delete')
    sql.append('from')
    sql.append(table)

    if kwargs.get('condition'):
        sql.append('where')
        sql.append(kwargs['condition'][3:])


    return '\r\n'.join(sql)


def get_select_sql(columns, table, **kwargs):
    sql = []
    sql.append("select")
    sql.append(columns)
    sql.append("from")
    sql.append(table)
    if kwargs.get('join'):
        sql.append(kwargs['join'])

    if kwargs.get('condition'):
        sql.append('where')
        sql.append(kwargs['condition'][3:])

    return "\r\n".join(sql)


def table_join(tableA, tableB, condition=''):

    if isinstance(tableA, dict) and \
       isinstance(tableB, dict) :
        sql = []
        tblA = __get_table_name(tableA)
        tblB = __get_table_name(tableB)

        sql.append(' inner join ')
        sql.append(tblB)
        sql.append(" on (")

        for i in  range(len(tableA[tblA])):
            if(i > 0):
                sql.append(str(condition))
            sql.append(" {0}.{1} = {2}.{3} ".format(tblA,
                                              tableA[tblA][i],
                                              tblB,
                                              tableB[tblB][i]))


        sql.append(")")
        return "".join(sql)

    return ""


def table_left_join(tableA, tableB, condition=''):

    if isinstance(tableA, dict) and \
       isinstance(tableB, dict) :
        sql = []
        tblA = __get_table_name(tableA)
        tblB = __get_table_name(tableB)

        sql.append(' left join ')
        sql.append(tblB)
        sql.append(" on (")
        for i in range(len(tableA[tblA])):
            if(i > 0):
                sql.append(str(condition))
            sql.append("{0}.{1} = {2}.{3} ".format(tblA,
                                              tableA[tblA][i],
                                              tblB,
                                              tableB[tblB][i]))


        sql.append(")")
        return "".join(sql)

    return ""


def table_right_join(tableA, tableB, condition=''):
    if isinstance(tableA, dict) and \
       isinstance(tableB, dict) :
        sql = []
        tblA = __get_table_name(tableA)
        tblB = __get_table_name(tableB)

        sql.append(' right join ')
        sql.append(tblB)
        sql.append(" on (")
        for i in range(len(tableA[tblA])):
            if(i > 0):
                sql.append(str(condition))
            sql.append("{0}.{1} = {2}.{3} ".format(tblA,
                                              tableA[tblA][i],
                                              tblB,
                                              tableB[tblB][i]))


        sql.append(")")
        return "".join(sql)

    return ""


def add_condition(conditions):
    sql = []

    for cond, tbl, col, oper in conditions:
        if oper == Operation.LIKE:
            condition = "{0}  {1}.{2} LIKE ?"
        else:
            condition = "{0}  {1}.{2} {3} ?"

        sql.append(condition.format(
            cond,
            tbl,
            col,
            oper
        ))

    return "\r\n".join(sql)


def __get_table_name(tbl):
    if isinstance(tbl, dict):
        for key in tbl.keys():
            return key
    return "tbl"
