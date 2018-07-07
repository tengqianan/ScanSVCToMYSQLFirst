import pymysql
import csv
import codecs
import glob
import pandas as pd

def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='teng',charset='gbk')
    return conn

def insert(cur,sql,args):
    cur.execute(sql,args)

def read_csv_to_mysql(filename):
    with codecs.open(filename=filename,mode='r',encoding='gbk') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into stock_csv VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            if item[1] is None or item[1] == '':
                continue
            args = tuple(item)
            print(args)
            insert(cur,sql=sql,args=args)
        conn.commit()
        cur.close()
        conn.close()

def hebing():
    csv_list = glob.glob('/Users/mac/stock/*.csv')
    print(u'共发现了%s个CSV文件'%len(csv_list))
    print(u'正在处理。。。。')
    for i in csv_list:
        f = open(i,'r',encoding='gbk')
        f.readline()
        fr = f.read()
        #print(fr)
        with open('stock.csv','a') as f:
            f.write(fr)
            f.close()

    print(u'写入完毕')

def quchong(file):
    df = pd.read_csv(file,header=0,encoding='gbk')
    datalist = df.drop_duplicates()
    datalist.to_csv()

if __name__ == '__main__':
    hebing()
    quchong("stock.csv")
    read_csv_to_mysql('stock.csv')

