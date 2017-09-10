from github import Github
from os import environ as env
N = 1

g = Github(env['GITHUB_USERNAME'], env['GITHUB_PASSWORD'])
repo = g.get_repo('louislai/dummy_repo')
for issue in repo.get_issues(state='closed'):
    if not issue.pull_request:
        continue
    print('Reopening PR ' + issue.title)
    issue.edit(state='open')

