import time
import win32com.client
import pypyodbc
url = r'C:\Users\lenovo\Desktop\数据库.mdb'
strD = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s'%url
# print(str)
db = pypyodbc.win_connect_mdb(strD)
curser = db.cursor()
curser.execute("SELECT id from FSL where 埋设方式 = '管块'")
for col in curser.description:                          # 显示行描述
    print (col[0], col[1])
result = curser.fetchall()
print(result)

sql = "select id,总孔数,已用孔数 from FSL where id in (SELECT id from FSL where 埋设方式 = '管块')"
curser.execute(sql)
result = curser.fetchall()
print(result)
for i in range(len(result)):
    a = result[i][1]
    b = result[i][2]
    id = result[i][0]
    if a < b:
        print('管块孔数错误','id=',id)
import  re
curser.execute("SELECT 管径 from FSL WHERE 管径 IS NOT NULL ")
result = curser.fetchall()
print(result,'管径')
for i in range(len(result)):
    a = result[i][0]
    res = re.findall("[^0-9X]",a)
    print(res)
    if res:
        print('管径错误',i+1)
    else:
        print('管径正常')

print('-----'*30)
# curser.execute("SELECT id from FSL where 材质 ='' ")
curser.execute("SELECT id from FSL where [材质]='' or [材质] is NULL ")
result = curser.fetchall()
print(result)
if result:
    list = []
    for i in range(len(result)):
        list.append(result[i][0])
    list = [str(i) for i in list]
    a = ','.join(list)
    print(a)
    sql = 'select id,电缆条数,光缆条数,管线使用状况,线型 from FSL where id in (%s)'%a
    curser.execute(sql)
    result = curser.fetchall()
    print(result)
    for i in range(len(result)):
        id = result[i][0]
        dl = result[i][1]
        gl = result[i][2]
        stu = result[i][3]
        types = result[i][4]
        if dl and gl:
            print('电缆光缆存在数据','id=',id)
        if stu !='空管' and types !='预埋管线':
            print('管线使用状况、线型错误','id=',id)
# sql = 'SELECT id from FSL where 材质 IS null '
# curser.execute(sql)
# result = curser.fetchall()
# print(result)
print('-----'*30)
curser.execute("SELECT 建设日期,管线权属单位,所在位置,工程编号,工程类别,勘测单位,测量时间,管线范畴,更新状态 from FSL")
result = curser.fetchall()
print(result)
model = result[0]
for i in range(len(result)):
    id = i+1
    if result[i] == model:
        print('OK',id)
    else:
        print('NG',id)
curser.execute("SELECT 建设日期,管线权属单位,所在位置,工程编号,工程类别,勘测单位,测量时间,管点范畴,更新状态,获取时机 from FSP")
result = curser.fetchall()
print(result)
model = result[0]
for i in range(len(result)):
    id = i+1
    if result[i] == model:
        print('OK',id)
    else:
        print('NG',id)
print('-----'*30)
# def
curser.execute("SELECT id,起点埋深,终点埋深 from FSL where 起点点号 in (select 起点点号 from FSP WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')")
result = curser.fetchall()
print(result)
for i in range(len(result)):
    a = result[i][1]
    b = result[i][2]
    id = result[i][0]
    if a != b:
        print('起点埋深、终点埋深错误','id=',id)