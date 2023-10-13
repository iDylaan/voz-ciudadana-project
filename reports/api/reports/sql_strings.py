class Sql_Strings():
    GET_REPORTS = (
        "SELECT "
        "r.*, "
        "GROUP_CONCAT(ri.image_url) AS images "
        "FROM reports r "
        "LEFT JOIN report_images ri ON r.id = ri.report_id "
        "GROUP BY r.id"
    )
    
    GET_REPORT_BY_ID = (
        "SELECT r.*, "
        "GROUP_CONCAT(ri.image_url) AS images "
        "FROM reports r "
        "LEFT JOIN report_images ri ON r.id = ri.report_id "
        "WHERE r.id = %(id_report)s "
        "GROUP BY r.id"
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
    
    INSERT_REPORT_IMAGES = (
        "INSERT INTO report_images (image_url, report_id) "
        "VALUES {}"
    )
    
    UPDATE_REPORT = (
        "UPDATE reports SET "
        "report_title = %(report_title)s, "
        "report_description = %(report_description)s, "
        "category_id = %(category_id)s "
        "WHERE id = %(id_report)s"
    )
    
    
    LOGIC_DELETE_REPORT = (
        "UPDATE reports SET "
        "status_id = 4"
    )