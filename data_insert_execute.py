import requests,sys,os,time,json
from test_example import Mysql
from itertools import islice

with open("C:\\Users\\lijy1427\\Documents\\Tencent Files\\1185805992\\FileRecv\\gti201806.txt",'r',encoding='gbk') as file:
 # for line in islice(file,1,None):
   next(file)
   for line in file.readlines():
        start_date = 'null'
        call_number = 'null'
        called_number = 'null'
        time_duration = 'null'
        fee = 'null'
        if line:
            list = []
            list = line.encode('utf-8').decode('utf-8-sig').strip('\n').split(",")
            start_date = list[0]
            call_number = list[1]
            called_number = list[2]
            time_duration = (list[3])
            fee = list[4]
            sql = """
                     insert into gti_201806 (start_date,call_number,called_number,time_duaration,fee) VALUES ('%s','%s','%s','%s','%s')"""

            try:
                mysql = Mysql()
                mysql.execute_no_query(sql % (start_date,call_number,called_number,time_duration,fee))
            except Exception as e:
                print(e)
            finally:
               mysql.db_close()
        else:
            break
