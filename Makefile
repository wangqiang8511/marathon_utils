all: buildenv ensure_dir

test: buildenv buildenvtest runtest

buildenv:
	virtualenv .
	bin/pip install -r requirements.txt

buildenvtest:
	bin/pip install -r test_requirements.txt

runtest:
	bin/nosetests -s

install: 
	pip install -r requirements.txt

ensure_dir:
	mkdir -p var/log
	mkdir -p var/run
	chmod -R a+w var

docker: 
	./build_docker

clean:
	rm -rf lib lib64 bin share include man var
	find . -name '*.pyc' | awk '{print "rm -f "$$1}' | sh
