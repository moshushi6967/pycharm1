import pymysql as mdb
import time
start=time.time()
def createTrain():
    try:
        con=mdb.connect('localhost', 'root', 'root', 'it',charset='utf8');
        with con:
              cur = con.cursor()
              file= open("C:\\Users\\lijy1427\\Documents\\Tencent Files\\1185805992\\FileRecv\\gti201806.txt",'r', encoding='gbk')
              next(file)
              array=[]
              for line in file.readlines():
                list = line.encode('utf-8').decode('utf-8-sig').strip('\n').split(",")
                value = (list[0],list[1],list[2],list[3],list[4])
                array.append(value)
              sql="INSERT INTO gti_201806 VALUES(%s,%s,%s,%s,%s)"
              cur.executemany(sql,array)
              con.commit()
              cur.close()
    except mdb.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
createTrain()
print(time.time()-start)
print("done")
