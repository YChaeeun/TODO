import pymysql
from database import connection

# 해야 할 일 내용 가져오기
# 최근에 작성된 순서대로 
def get_todolist():
    conn = connection.get_connection()

    # start_idx = (int(page)-1)*10 

    sql = '''
        select todo_content, todo_importance
        from todo
        where todo_status = 1
        order by todo_idx desc
    ''' 

    cursor = conn.cursor()
    cursor.execute(sql)
    # cursor.execute(sql, (start_idx))

    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_dic = {
            'todo_content' : obj[0],
            'todo_importance' : obj[1]
        }
        data_list.append(data_dic)
    
    conn.close

    return data_list


# 할일 작성하기
def write_todo(element):
    conn = connection.get_connection()

    sql = '''
        insert into todo
        (todo_content, todo_status, todo_importance)
        values(%s, 1, 0)

    '''

    cursor = conn.cursor()
    cursor.execute(sql, element)

    conn.commit()
    conn.close()


# 할일 삭제 (상태값 변경)

# 할일 수정