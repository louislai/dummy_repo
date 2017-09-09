from github import Github
from os import environ as env

g = Github(env['GITHUB_USERNAME'], env['GITHUB_PASSWORD'])
repo = g.get_repo('louislai/dummy_repo')
for issue in repo.get_issues(state='open'):
    if not issue.pull_request:
        continue
    print('Cleaning PR ' + issue.title)
    # Remove label
    issue.edit(assignee=None, labels=[])
    for comment in issue.get_comments():
        comment.delete()

