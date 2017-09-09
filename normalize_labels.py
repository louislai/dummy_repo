from github import Github
from os import environ as env

g = Github(env['GITHUB_USERNAME'], env['GITHUB_PASSWORD'])
repo = g.get_user().get_repo('dummy_repo')
for issue in repo.get_issues(state='open'):
    if not issue.pull_request:
        continue
    print('Normalizing PR ' + issue.title)
    # Remove label
    labels = set([])
    for label in issue.get_labels():
        if label.name in labels:
            label.delete()
        else:
            labels.add(label.name)
