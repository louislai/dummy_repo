#!/bin/sh

curl --user "$GITHUB_USERNAME:$GITHUB_PASSWORD" --request POST --data '["test"]' https://api.github.com/repos/louislai/dummy_repo/issues/200/labels &
curl --user "$GITHUB_USERNAME:$GITHUB_PASSWORD" --request POST --data '["test"]' https://api.github.com/repos/louislai/dummy_repo/issues/199/labels
