class Sql_Strings():
    GET_FIRST_ACCESS_BY_USER_ID = (
        "SELECT firts_access "
        "FROM users "
        "WHERE id = %(id_user)s "
        "AND is_active = 1"
    )