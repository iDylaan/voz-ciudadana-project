class Sql_Strings():
    GET_REPORTS = (
        "SELECT "
        "r.*, "
        "GROUP_CONCAT(ri.image_url) AS images "
        "FROM reports r "
        "LEFT JOIN report_images ri ON r.id = ri.report_id "
        "WHERE ri.is_active = 1 "
        "GROUP BY r.id"
    )
    
    GET_REPORT_BY_ID = (
        "SELECT r.*, "
        "GROUP_CONCAT(ri.image_url) AS images "
        "FROM reports r "
        "LEFT JOIN report_images ri ON r.id = ri.report_id "
        "WHERE r.id = %(id_report)s "
        "AND ri.is_active = 1 "
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
    
    INSERT_REPORT_IMAGE = (
        "INSERT INTO report_images (image_url, report_id, is_active) "
        "VALUES (%(url_image)s, %(id_report)s, 1)"
    )
    
    GET_USER_BY_ID = (
        "SELECT id, username FROM users "
        "WHERE id = %(id_user)s "
    )
    
    CONFIRM_REPORT = (
        "INSERT INTO report_confirmations (report_id, user_id) "
        "VALUES (%(id_report)s, %(id_user)s) "
    )
    SET_CONFIRM_REPORT = (
        "UPDATE report_confirmations SET "
        "unconfirmed = 0, confirmed_dt = CURRENT_TIMESTAMP "
        "WHERE report_id = %(id_report)s "
        "AND user_id = %(id_user)s "
    )
    
    UNCONFIRM_REPORT = (
        "UPDATE report_confirmations SET "
        "unconfirmed = 1 "
        "WHERE user_id = %(id_user)s "
        "AND report_id = %(id_report)s "
    )
    
    
    LOGIC_DELETE_REPORT = (
        "UPDATE reports SET "
        "status_id = 4"
    )
    
    GET_REPORT_IMAGE_BY_ID = (
        "SELECT * FROM report_images "
        "WHERE id = %(id_image)s "
        "AND is_active = 1"
    )
    
    LOGIC_DELETE_REPORT_IMAGE = (
        "UPDATE report_images SET "
        "is_active = 0 "
        "WHERE id = %(id_image)s"
    )
    
    GET_IMAGE_BY_ID = (
        "SELECT * FROM report_images "
        "WHERE id = %(id_image)s "
    )
    
    GET_CONFIRMATION_BY_REPORT_AND_USER = (
        "SELECT * FROM report_confirmations "
        "WHERE report_id = %(id_report)s AND user_id = %(id_user)s"
    )

    GET_FIXED_CONFIRMATION_BY_REPORT_AND_USER = (
        "SELECT * FROM report_fixed_confirmations "
        "WHERE report_id = %(id_report)s AND user_id = %(id_user)s"
    )
    
    
    FIXED_CONFIRM_REPORT = (
        "INSERT INTO report_fixed_confirmations (report_id, user_id) "
        "VALUES (%(id_report)s, %(id_user)s) "
    )
    
    SET_FIXED_CONFIRM_REPORT = (
        "UPDATE report_fixed_confirmations SET "
        "unconfirmed = 0, confirmed_dt = CURRENT_TIMESTAMP "
        "WHERE report_id = %(id_report)s "
        "AND user_id = %(id_user)s "
    )
    
    FIXED_UNCONFIRM_REPORT = (
        "UPDATE report_fixed_confirmations SET "
        "unconfirmed = 1 "
        "WHERE user_id = %(id_user)s "
        "AND report_id = %(id_report)s "
    )