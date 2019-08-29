import paramiko
import time

start = time.time()
local_path='C:/Users/lijy1427/Documents/Tencent Files/1185805992/FileRecv/readme.txt'

def main():
    try:
        t = paramiko.Transport(('132.121.1.12',22))
        t.connect(username='zhjs',password='Awk@2018')
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get('/home/zhjs/gti201807.txt', local_path, callback=None)
        t.close()
        print('花费时间：', time.time() - start)
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    resulet = main()
    if resulet:
        print('下载文件 %s 成功'%local_path)
    else:
        print('下载文件 %s 失败' % local_path)