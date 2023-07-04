import pymysql

# исходная БД
# установление соединения с исходной БД
sourse_con = pymysql.connect(
    host='localhost',
    user='root',
    password='19980723',
    database='test_1',
)

old_list = []
# применение курсора исходной БД
with sourse_con:
    sourse_cur = sourse_con.cursor()
    sourse_cur.execute("SELECT * FROM test_1.categories")
    data = sourse_cur.fetchall()
    for i in data:
        old_list.append(i)


# целевая БД
target_con = pymysql.connect(
    host='localhost',
    user='root',
    password='19980723',
    database='new_database',
)

with target_con:
    target_cur = target_con.cursor()
    insert_query = "INSERT INTO new_categories (`id`, `parent_id`, `group_id`, `lvl`, `section_id`, `name`, `text`, `alias`, `meta_title`, `meta_description`, `meta_keywords`, `status`, `position`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for i in old_list:
        print(i)
        target_cur.execute(insert_query,
                           (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
    target_con.commit()

# with target_con:
#     target_cur = target_con.cursor()

# target_cur.execute("CREATE DATABASE IF NOT EXISTS new_database")
# target_cur.execute("USE new_database")
# create_table_query = '''CREATE TABLE new_categories (
#     id INT NOT NULL,
#     parent_id INT NULL,
#     group_id INT NULL,
#     lvl INT NULL,
#     section_id INT NULL,
#     name VARCHAR(250) NULL,
#     text VARCHAR(250) NULL,
#     alias VARCHAR(250) NULL,
#     meta_title VARCHAR(250) NULL,
#     meta_description VARCHAR(250) NULL,
#     meta_keywords VARCHAR(250) NULL,
#     status INT NULL,
#     position INT NULL
# )
# '''
# target_cur.execute(create_table_query)
# target_con.commit()
