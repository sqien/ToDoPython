import pymysql.cursors


connection = pymysql.connect(host = 'localhost',
                             port = 3306,
                             user = 'root',
                             password = '',
                             database = 'todolist',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connection.commit()

with connection.cursor() as cursor:
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
