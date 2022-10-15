import pymysql

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标        
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            # 提交数据库并执行        
            self.conn.commit()
        except Exception as ex:
            # 如果出意外的话就执行rollback()回滚到之前的状态
            self.conn.rollback()
            raise ex
        finally:
            # 关闭游标        
            self.cur.close()
            # 关闭数据库连接        
            self.conn.close()


if __name__ == '__main__':
    with DB(host='192.168.10.8',user='test',passwd='test',db='test') as db:
        db.execute('select * from employee')
        print(db)
        for i in db:
            print(i)
