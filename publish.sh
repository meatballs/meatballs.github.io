# vagrant ssh -c "cd /vagrant; make rsync_upload"
vagrant ssh -c "cd /vagrant; ghp-import output"
git push github gh-pages:master
