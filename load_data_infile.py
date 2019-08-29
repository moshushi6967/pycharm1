import pymysql

infohash_file_name = "readme.txt"
infohash_file_path = "C:"


def db_excute(sql):
    db = pymysql.connect("localhost", "root", "root", "it", local_infile=1)
    db.set_charset('utf8')
    cursor = db.cursor()
    print("connect correct")
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
    finally:
        db.close()


# 导入infohash数据到mysql xl_log_analysis 表
def LoadFile1(infohash_file_path='', infohash_file_name=''):
    # '''load data local infile "/root/test/infohash.txt_20180603" into table xl_log_analysis.infohash_20180603   LINES TERMINATED BY '\r\n'  (infohash);'''
    # '''LINES TERMINATED BY \\r\\n WIN 为\\r,LINUX 为\\n'''

    sql = " load data local infile '" \
          + infohash_file_path + "/" \
          + infohash_file_name + "'" + \
          " into table gti_201806" \
          " character set gbk"\
          " FIELDS TERMINATED BY ',' "\
          " LINES TERMINATED BY '\\r' " \
          " ignore 1 lines" \
          "; "
    db_excute(sql)
    print(sql)


if __name__ == '__main__':
    LoadFile1(infohash_file_path, infohash_file_name)