PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=/vagrant
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=192.168.3.4
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www/owencampbell.org.uk

GITHUB_ALIAS=github
GITHUB_PAGES_BRANCH=gh-pages
GITHUB_PUBLISH_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

html:
	vagrant ssh -c "cd /vagrant; $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)"

clean:
	vagrant ssh -c "cd /vagrant; [ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)"

regenerate:
	vagrant ssh -c "cd /vagrant; $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)"

publish:
	vagrant ssh -c "cd /vagrant; $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)"

ssh_upload: publish
	vagrant ssh -c "cd /vagrant; scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)"

rsync_upload: publish
	vagrant ssh -c "cd /vagrant; rsync -e 'ssh -p $(SSH_PORT)'' -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude"

github: publish
	vagrant ssh -c "cd /vagrant; ghp-import -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)"
	git push $(GITHUB_ALIAS) $(GITHUB_PAGES_BRANCH):$(GITHUB_PUBLISH_BRANCH)

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
