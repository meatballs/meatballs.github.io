# vagrant ssh -c "cd /vagrant; make rsync_upload"
vagrant ssh -c "cd /vagrant; pelican content -o output -s publishconf.py; ghp-import output"
git push github gh-pages:master
