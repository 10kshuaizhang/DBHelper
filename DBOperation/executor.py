# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2022/7/27'

import os
import re

PTAH_TO_REPO = "/Users/shuaizhang/Downloads/database"
CLONE_PATH = "https://github.com/10kshuaizhang/database.git"
PATTERN = ".sql"
RELEASE_NUMBER = "327"
inner_folders = ("alter_table/", "pre_release/")
inner_table_folders = ("global/", "shards/")
DBs = ['test']

# def update_release(path_to_repo, release_number):
#     base_path = path_to_repo + "/release_" + release_number + "/0/migration/"
#     for relpath, _, files in os.walk(base_path):
#         for file in files:
#             if file.endswith(pattern):
#                 full_path = os.path.join(base_path, relpath, file)
#                 execute_sql_file(os.path.normpath(os.path.abspath(full_path)), "db_name")
#                 # execute_sql_file(path + file, "shard_db_name")

# def update_release_range(start, end):
#     pass


def get_sql_files(path_to_repo, release_number):
    target_files = []
    base_path = path_to_repo + "/release_" + release_number + "/0/migration/"
    for relpath, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(PATTERN):
                full_path = os.path.join(base_path, relpath, file)
                target_files.append(os.path.normpath(os.path.abspath(full_path)))
    return target_files


# def get_all_sql_files(path_to_repo):
#     target_files = []
#
#     base_path = path_to_repo + "/release_" + release_number + "/0/migration/"


def execute(filename, cursor):
    with open(filename, 'r') as f:
        content = f.read()
        sqls = [sql for sql in content.split(';') if re.match("\S", sql)]

        for sql in sqls:
            try:
                cursor.execute(sql)
                data = cursor.fetchone()
            except Exception as msg:
                print("error: ", msg)
    print('Finish execute ' + filename.split("/")[-1])


def execute_sql_file(files, dbs):
    import pymysql
    for db_name in dbs:
        connection = pymysql.connect(host='localhost', user='root', password='zhangshuai',
                                 port=3306, db=db_name, charset='utf8')
        cursor = connection.cursor()
        for file in files:
            execute(file, cursor)
            connection.commit()
        connection.close()


if __name__ == "__main__":
    # print(get_sql_files(PTAH_TO_REPO, RELEASE_NUMBER))
    execute_sql_file(get_sql_files(PTAH_TO_REPO, RELEASE_NUMBER), DBs)
