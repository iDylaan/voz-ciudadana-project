class Sql_Strings():
    GET_REPORTS = (
        "SELECT "
        "r.*, "
        "rc.category_name, "
        "rs.status_name, "
        "u.username, "
        "GROUP_CONCAT( "
            "IFNULL( "
                "JSON_OBJECT('id', ri.id, 'image', ri.image_url), "
                "'' "
            ") SEPARATOR '|' "
        ") AS images "
        "FROM REPORTS r "
        "LEFT JOIN REPORT_IMAGES ri ON r.id = ri.report_id AND ri.is_active = 1 "
        "LEFT JOIN REPORT_CATEGORIES rc ON r.category_id = rc.id "
        "LEFT JOIN REPORT_STATUS rs ON r.status_id = rs.id "
        "LEFT JOIN USERS u ON r.user_id = u.id "
        "WHERE r.status_id = 2 "
        "AND u.is_active = 1 "
        "GROUP BY r.id "
        "ORDER BY r.creation_dt DESC"
    )
    
    GET_REPORT_BY_ID = (
        "SELECT "
        "r.*, "
        "rc.category_name, "
        "rs.status_name, "
        "u.username, "
        "GROUP_CONCAT( "
            "IFNULL( "
                "JSON_OBJECT('id', ri.id, 'image', ri.image_url), "
                "'' "
            ") SEPARATOR '|' "
        ") AS images "
        "FROM REPORTS r "
        "LEFT JOIN REPORT_IMAGES ri ON r.id = ri.report_id AND ri.is_active = 1 "
        "LEFT JOIN REPORT_CATEGORIES rc ON r.category_id = rc.id "
        "LEFT JOIN REPORT_STATUS rs ON r.status_id = rs.id "
        "LEFT JOIN USERS u ON r.user_id = u.id "
        "WHERE r.id = %(id_report)s "
        "AND r.status_id IN (1, 2) "
        "AND u.is_active = 1 "
        "GROUP BY r.id"
    )

    GET_USER_REPORTS = (
        "SELECT "
        "r.*, "
        "rc.category_name, "
        "rs.status_name, "
        "u.username, "
        "GROUP_CONCAT( "
            "IFNULL( "
                "JSON_OBJECT('id', ri.id, 'image', ri.image_url), "
                "'' "
            ") SEPARATOR '|' "
        ") AS images "
        "FROM REPORTS r "
        "LEFT JOIN REPORT_IMAGES ri ON r.id = ri.report_id AND ri.is_active = 1 "
        "LEFT JOIN REPORT_CATEGORIES rc ON r.category_id = rc.id "
        "LEFT JOIN REPORT_STATUS rs ON r.status_id = rs.id "
        "LEFT JOIN USERS u ON r.user_id = u.id "
        "WHERE r.user_id = %(id_user)s "
        "AND u.is_active = 1 "
        "GROUP BY r.id"
    )
    
    INSERT_REPORT = (
        "INSERT INTO REPORTS "
        "("
            "report_title, "
            "report_description, "
            "user_id, "
            "category_id, "
            "status_id, "
            "last_updated_dt, "
            "creation_dt, "
            "coords "
        ") VALUES "
        "("
            "%(report_title)s, "
            "%(report_description)s, "
            "%(user_id)s, "
            "%(category_id)s, "
            "%(status_id)s, "
            "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "
            "%(coords)s"
        ")" 
    )
    
    INSERT_REPORT_IMAGES = (
        "INSERT INTO REPORT_IMAGES (image_url, report_id, is_active) "
        "VALUES {}"
    )
    
    UPDATE_REPORT = (
        "UPDATE REPORTS SET "
        "report_title = %(report_title)s, "
        "report_description = %(report_description)s, "
        "category_id = %(category_id)s, "
        "coords = %(coords)s, "
        "last_updated_dt = CURRENT_TIMESTAMP "
        "WHERE id = %(id_report)s"
    )
    
    INSERT_REPORT_IMAGE = (
        "INSERT INTO REPORT_IMAGES (image_url, report_id, is_active) "
        "VALUES (%(url_image)s, %(id_report)s, 1)"
    )
    
    GET_USER_BY_ID = (
        "SELECT id, username FROM USERS "
        "WHERE id = %(id_user)s "
    )
    
    CONFIRM_REPORT = (
        "INSERT INTO REPORT_CONFIRMATIONS (report_id, user_id) "
        "VALUES (%(id_report)s, %(id_user)s) "
    )
    SET_CONFIRM_REPORT = (
        "UPDATE REPORT_CONFIRMATIONS SET "
        "unconfirmed = 0, confirmed_dt = CURRENT_TIMESTAMP "
        "WHERE report_id = %(id_report)s "
        "AND user_id = %(id_user)s "
    )
    
    UNCONFIRM_REPORT = (
        "UPDATE REPORT_CONFIRMATIONS SET "
        "unconfirmed = 1 "
        "WHERE user_id = %(id_user)s "
        "AND report_id = %(id_report)s "
    )
    
    
    LOGIC_DELETE_REPORT = (
        "UPDATE REPORTS SET "
        "status_id = 4 "
        "WHERE id = %(id_report)s "
    )
    
    GET_REPORT_IMAGE_BY_ID = (
        "SELECT * FROM REPORT_IMAGES "
        "WHERE id = %(id_image)s "
        "AND is_active = 1"
    )
    
    LOGIC_DELETE_REPORT_IMAGE = (
        "UPDATE REPORT_IMAGES SET "
        "is_active = 0 "
        "WHERE id = %(id_image)s"
    )
    
    GET_IMAGE_BY_ID = (
        "SELECT * FROM REPORT_IMAGES "
        "WHERE id = %(id_image)s "
    )
    
    GET_CONFIRMATION_BY_REPORT_AND_USER = (
        "SELECT * FROM REPORT_CONFIRMATIONS "
        "WHERE report_id = %(id_report)s AND user_id = %(id_user)s"
    )

    GET_FIXED_CONFIRMATION_BY_REPORT_AND_USER = (
        "SELECT * FROM REPORT_FIXED_CONFIRMATIONS "
        "WHERE report_id = %(id_report)s AND user_id = %(id_user)s"
    )
    
    
    FIXED_CONFIRM_REPORT = (
        "INSERT INTO REPORT_FIXED_CONFIRMATIONS (report_id, user_id) "
        "VALUES (%(id_report)s, %(id_user)s) "
    )
    
    SET_FIXED_CONFIRM_REPORT = (
        "UPDATE REPORT_FIXED_CONFIRMATIONS SET "
        "unconfirmed = 0, confirmed_dt = CURRENT_TIMESTAMP "
        "WHERE report_id = %(id_report)s "
        "AND user_id = %(id_user)s "
    )
    
    FIXED_UNCONFIRM_REPORT = (
        "UPDATE REPORT_FIXED_CONFIRMATIONS SET "
        "unconfirmed = 1 "
        "WHERE user_id = %(id_user)s "
        "AND report_id = %(id_report)s "
    )
    
    
    GET_CATEGORY_BY_ID = (
        "SELECT * FROM report_categories "
        "WHERE id = %(category_id)s"
    )
    
    GET_PENDING_REPORTS = (
        "SELECT "
        "r.*, "
        "rc.category_name, "
        "rs.status_name, "
        "u.username, "
        "GROUP_CONCAT( "
            "IFNULL( "
                "JSON_OBJECT('id', ri.id, 'image', ri.image_url), "
                "'' "
            ") SEPARATOR '|' "
        ") AS images "
        "FROM REPORTS r "
        "LEFT JOIN REPORT_IMAGES ri ON r.id = ri.report_id AND ri.is_active = 1 "
        "LEFT JOIN REPORT_CATEGORIES rc ON r.category_id = rc.id "
        "LEFT JOIN REPORT_STATUS rs ON r.status_id = rs.id "
        "LEFT JOIN USERS u ON r.user_id = u.id "
        "WHERE r.status_id = 1 "
        "AND u.is_active = 1 "
        "GROUP BY r.id "
        "ORDER BY r.creation_dt DESC"
    )
    
    ACTIVATE_REPORT_BY_ID = (
        "UPDATE reports SET status_id = 2 WHERE id = %(id_report)s"
    )
    
    DECLINATE_REPORT_BY_ID = (
        "UPDATE reports SET status_id = 4 WHERE id = %(id_report)s"
    )