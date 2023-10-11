class Sql_Strings():
    GET_REPORTS = (
        "SELECT * FROM reports"
    )
    
    GET_REPORT_BY_ID = (
        "SELECT * FROM reports "
        "WHERE id = %(id_report)s"
    )
    
    INSERT_REPORT = (
        "INSERT INTO reports "
        "("
            "report_title, "
            "report_description, "
            "user_id, "
            "category_id, "
            "status_id, "
            "last_updated_dt, "
            "creation_dt "
        ") VALUES "
        "("
            "%(report_title)s, "
            "%(report_description)s, "
            "%(user_id)s, "
            "%(category_id)s, "
            "%(status_id)s, "
            "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP"
        ")" 
    )
    
    GET_REPORT_BY_ID = (
        "SELECT * FROM reports "
        "WHERE id = %(id_report)s "
    ) 
    
    INSERT_REPORT_IMAGES = (
        "INSERT INTO report_images (image_url, report_id) "
        "VALUES {}"
    )