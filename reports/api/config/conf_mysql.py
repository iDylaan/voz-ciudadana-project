import pymysql
from api import api

def query(qry, params=None, get_one=False):
    conn = conn_mysql()
    if conn is None:
        return None
    try:
        with conn.cursor() as cursor:
            if params:
                cursor.execute(qry, params)
            else:
                cursor.execute(qry)
            conn.commit()
            result = cursor.fetchone() if get_one else cursor.fetchall()
            if not result:
                return {"status": "NOT_FOUND"} 
            return {"status": "OK", "data": result}
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_mysql/{}".format(e))
        return {"status": "Error"}
    finally:
        cursor.close()
        conn.close()
        
def sql(qry, params=None):
    conn = conn_mysql()
    if conn is None:
        return None
    try:
        with conn.cursor() as cursor:
            if params:
                cursor.execute(qry, params)
            else:
                cursor.execute(qry)
            conn.commit()
            result = cursor.fetchone()
            return {"status": "OK", "last_insert_id": cursor.lastrowid}
    except Exception as e:
        print("Ha ocurrido un error en el query @query.conf_mysql/{}".format(e))
        return {"status": "Error"}
    finally:
        cursor.close()
        conn.close()


def conn_mysql():
    config = {
        'host': api.config['MYSQL_HOST'],
        'port': int(api.config['MYSQL_PORT']),
        'user': api.config['MYSQL_USER'],
        'password': api.config['MYSQL_PASS'],
        'database': api.config['MYSQL_DB'],
        'charset': api.config['MYSQL_CHARSET'],
        'cursorclass': pymysql.cursors.DictCursor
    }
    try: 
        conn = pymysql.connect(**config)
    except Exception as e:
        print("Ha ocurrido un error al conectar en @conn_mysql.conf_mysql/{}".format(e))
        return None
    return conn