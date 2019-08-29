import pymysql

infohash_file_name = "gti201806.txt"
infohash_file_path = "C:/Users/lijy1427/Documents/Tencent Files/1185805992/FileRecv"
# 执行语句
def db_excute(sql):
    # local_infile = 1 执行load data infile
    db = pymysql.connect("localhost", "root", "root", "it", local_infile=1)
    db.set_charset('utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
    finally:
        db.close()
def LoadFile1(infohash_file_path='', infohash_file_name=''):
    # '''load data local infile "/root/test/infohash.txt_20180603" into table xl_log_analysis.infohash_20180603   LINES TERMINATED BY '\r\n'  (infohash);'''
    # '''LINES TERMINATED BY \\r\\n WIN 为\\r,LINUX 为\\n'''
    sql = " load data local infile '" \
          + infohash_file_path + "/" \
          + infohash_file_name + "'" + \
          " into table gti_201806" \
          " character set gbk"\
          " FIELDS TERMINATED BY ',' "\
          " LINES TERMINATED BY '\\n' " \
          " ignore 1 lines" \
          "; "
    db_excute(sql)
    print(sql)

if __name__ == '__main__':
    LoadFile1(infohash_file_path, infohash_file_name)