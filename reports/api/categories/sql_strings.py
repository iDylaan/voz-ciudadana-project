class Sql_Strings():
    GET_CATEGORIES = (
        "SELECT * FROM report_categories rc "
        "ORDER BY " 
        "    CASE "
        "        WHEN rc.category_name = 'OTRO' THEN 1 "
        "        ELSE 0 "
        "    END, " 
        "    rc.category_name"
    )