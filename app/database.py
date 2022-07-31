import mysql.connector

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = 'mysql',
              user = 'mysql',
              passwd = 'password',
              db = 'main'
      )
      return conn

def insert_ai_analysis_log(image_path, success, message, estimated_class, confidence,request_timestamp, response_timestamp):
    sql = f"INSERT INTO ai_analysis_log (image_path, success, message, class, confidence,request_timestamp, response_timestamp) \
        VALUES ('{image_path}', '{success}', '{message}', '{estimated_class}', '{confidence}','{request_timestamp}', '{response_timestamp}')"
    
    conn = conn_db()
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql)
    cursor.execute("SELECT * FROM ai_analysis_log")
    result = cursor.fetchall()[-1]
    conn.commit()
    cursor.close()
    conn.close()

    return result