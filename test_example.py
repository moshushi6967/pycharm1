import pandas as pd
"""
  利用pandas读取txt文件
"""
def main():
    path = 'C:\\Users\\lijy1427\\Documents\\Tencent Files\\1185805992\\FileRecv\\C01001MAWANGJIEX2019061000000.051\\C01001MAWANGJIEX2019061000000.051'
    data = pd.read_table(path,sep='|',header=None,encoding='gbk').head(n=3)
    print(type(data))
    print(data)

if __name__ == '__main__':
    main()