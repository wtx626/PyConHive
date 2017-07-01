#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/28 14:56
# @Author  : wutianxiong
# @File    : hiveclient.py
# @Software: PyCharm

import pyhs2

class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):
        """
        query
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetch()

    def close(self):
        """
        close connection
        """
        self.conn.close()


def main():
    """
    main process
    @rtype:
    @return:
    @note:

    """
    hive_client = HiveClient(db_host='10.0.3.1', port=10001, user='', password='',
                             database='test', authMechanism='NOSASL')
    result = hive_client.query('select * from ntciflow limit 10')
    print result
    hive_client.close()


if __name__ == '__main__':
    main()