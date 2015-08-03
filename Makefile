include VERSION

all: buildenv ensure_dir

test: buildenv buildenvtest runtest

install: ensure_dir buildenv

buildenv:
	virtualenv .
	bin/pip install -r requirements.txt

buildenvtest:
	bin/pip install -r test_requirements.txt

runtest:
	bin/nosetests -s

ensure_dir:
	mkdir -p var/log
	mkdir -p var/run
	chmod -R a+w var

docker: 
	docker build -t $(REPO):$(VERSION) .

clean:
	rm -rf lib lib64 bin share include man var
	find . -name '*.pyc' | awk '{print "rm -f "$$1}' | sh
