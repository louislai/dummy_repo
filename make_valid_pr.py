from github import Github
from os import environ as env

g = Github(env['GITHUB_USERNAME'], env['GITHUB_PASSWORD'])
repo = g.get_user().get_repo('dummy_repo')
for issue in repo.get_issues(state='open'):
    if not issue.pull_request:
        continue
    print('Make valid PR ' + issue.title)
    # Remove label
    issue.edit(assignee=None, labels=[], title='[W3.3][W14-1]' + str(issue.id))
    for comment in issue.get_comments():
        comment.delete()

