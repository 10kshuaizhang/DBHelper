# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2022/7/28'

from GitOperation.puller import download_git
from DBOperation.executor import *

PTAH_TO_REPO = "/Users/shuaizhang/Downloads/database"
CLONE_PATH = "https://github.com/10kshuaizhang/database.git"
BRANCH_NAME = "main"
PATTERN = ".sql"
# RELEASE_NUMBER = 327
DBs = ["test"]


download_git(PTAH_TO_REPO, CLONE_PATH, BRANCH_NAME)
execute_sql_file(get_sql_files(PTAH_TO_REPO, RELEASE_NUMBER), DBs)
