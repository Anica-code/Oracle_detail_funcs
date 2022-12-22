def table_names(con, db, user_name=None):
    """Function returns a list of table names of the specified database

            con: Connection to Oracle environment
            db: Database name
            user_name: Defaults to None. If specified, it returns the table names of a specific user"""

    cur = con.cursor()

    if user_name is None:
        cur.execute(f"SELECT table_name FROM {db}")
    else:
        cur.execute(f"SELECT table_name FROM {db} WHERE user={user_name}")

    table_list = []

    for row in cur:
        name = cur[0]
        table_list.append(name)

    return table_list
