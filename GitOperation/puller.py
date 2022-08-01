# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2022/7/26'

import os
import git


def download_git(download_path, clone_path, branch_name):
    # 从远程仓库更新代码
    if os.listdir(download_path):
        print('git pull to ', download_path)
        repo = git.Repo(download_path)

        # 切换到最新分支
        repo.git.checkout(branch_name)
        repo.git.pull()
        cur_branch = repo.git.branch()
        print('current branch ', cur_branch, ' 代码正在拉取中...')
    # 从远程仓库下载代码
    else:
        print('clone from ', clone_path)
        git.Repo.clone_from(clone_path, to_path=download_path, branch='master')


if __name__ == "__main__":
    path_to_repo = "/Users/shuaizhang/Downloads/database"
    clone_path = "https://github.com/10kshuaizhang/database.git"
    branch_name = "main"
    download_git(path_to_repo, clone_path, branch_name)
