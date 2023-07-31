#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

# navigate into the build output directory
cd dist

# initialize a new temporary Git repository
git init

# add all files to the new repository
git add -A

# commit the changes
git commit -m 'deploy'

# push the changes to the gh-pages branch on GitHub
git push -f git@github.com:GUFFYch/site-project.git HEAD:gh-pages

# clean up
cd ..
rm -rf dist
