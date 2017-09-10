from github import Github
from os import environ as env
N = 1

g = Github(env['GITHUB_USERNAME'], env['GITHUB_PASSWORD'])
repo = g.get_repo('louislai/dummy_repo')
i = 0
for issue in repo.get_issues(state='open'):
    if not issue.pull_request:
        continue
    i += 1
    if i <= N:
        continue
    print('Cleaning PR ' + issue.title)
    issue.edit(state='closed')

