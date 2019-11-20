import pymssql
import _mssql


class DB:
    """
    基于MSSQL的数据库操作类
    """

    def __init__(self):
        """
        初始化数据库连接参数
        """
        self.host = '127.0.0.1:4000'
        self.user = 'aszyk'
        self.password = 'zyk-2019'
        self.database = 'public_doors'

    def get_conn_mssql(self):
        """
        初始化连接器
        """
        return _mssql.connect(server=self.host,
                              user=self.user,
                              password=self.password,
                              database=self.database)

    def get_conn_pymssql(self):
        """
        初始化连接器
        """
        return pymssql.connect(self.host,
                               self.user,
                               self.password,
                               self.database)

    def get_data_by_sql(self, sel_sql):
        """
        按查询语句查询出数据集，并返回数据集
        :param sel_sql:   查询语句
        :return:          查询结果
        """
        with self.get_conn_pymssql() as conn:
            with conn.cursor(as_dict=True) as cur:
                cur.execute(sel_sql)
                rows = cur.fetchall()
                return rows

    def execute_sql(self, exe_sql):
        """
        执行一条sql语句
        :param exe_sql:    执行语句
        :return:           成功返回true，失败返回false
        """
        with self.get_conn_pymssql() as conn:
            with conn.cursor() as cur:
                sta = cur.execute(exe_sql)
                if sta == 1:
                    conn.commit()
                    cur.close()
                    conn.close()
                    return True
                else:
                    return False

    def execute_sqls(self, sqls=None):
        """
        执行列表中的所有sql语句，然后统一提交
        :param sqls:  语句列表
        :return:
        """
        # print("begin")
        with self.get_conn_pymssql() as conn:
            with conn.cursor() as cur:
                for exe_sql in sqls:
                    print(exe_sql)
                    cur.execute(exe_sql)
                conn.commit()
                cur.close()
                conn.close()
        # print("end")

    def run_proc(self, proc_name, params=None):
        """
        调用存储过程 执行操作（增删改）
        proc_name 存储过程名称
        params     所带参数     元组
        """
        conn = self.get_conn_mssql()
        sqlcmd = """
        DECLARE @re smallint
        EXEC @re=""" + proc_name + ' '
        i = 0
        for param in params:
            if i < len(params) - 1:
                sqlcmd += "'" + param + "', "
            else:
                sqlcmd += "'" + param + "'"
            i += 1
        sqlcmd += """
        SELECT @re
        """
        try:
            re = conn.execute_scalar(sqlcmd)
        except _mssql.MssqlDatabaseException as e:
            print('调用存储过程失败：' + proc_name + ' ' + str(e))
            return 1
        finally:
            conn.close()
            return re

    def get_run_proc(self, proc_name, params=None):
        conn = self.get_conn_mssql()
        sqlcmd = """
                EXEC """ + proc_name + ' '
        i = 0
        for param in params:
            if i < len(params) - 1:
                sqlcmd += "'" + param + "', "
            else:
                sqlcmd += "'" + param + "'"
            i += 1
        try:
            print(sqlcmd)

            conn.execute_query(sqlcmd)
            res = []
            for row in conn:
                res.append(row)
        except _mssql.MssqlDatabaseException as e:
            print('调用存储过程失败：' + proc_name + ' ' + str(e))
            return 1
        finally:
            conn.close()
            return res


if __name__ == '__main__':
    db = DB()
    # wl = "select user_id, user_name from t_users"
    # da = db.get_data_by_sql(wl)
    # print(da)
    params = ('005', 'dalun', '系统管理员', '', '1')
    re_data = db.run_proc('add_user', params)
    print(re_data)
    # print("hello 222")
    # params = ('%', '%')
    # re_data = db.get_run_proc('get_users', params)
    # print(re_data[0]['user_name'])
    # print("hello 333")
