import mysql.connector
res = mysql.connector.connect(host="localhost",user="root",password="Sindhu@mysql",auth_plugin='mysql_native_password',database='klu')
cu=res.cursor()
'''
cu.execute("insert into cse values(4,'santhu')")
cu.execute("insert into cse values(2,'dhanu')")     #insertion
cu.execute("insert into cse values(3,'niha')")

sql="DELETE FROM  cse WHERE id='1'"      # deletion

sql="UPDATE cse set id='1',name='updated' where id='4'"   #updation

ret=cu.execute("select * from cse")
a=cu.fetchall()
for i in a:                    #retreving all the data in table
    print(i)

cu.execute()
res.commit()
'''
ret=cu.execute("select name from cse")
a=cu.fetchall()      # retreving specific data in table
for i in a:
    print(i)

cu.close()