.PHONY: test servers

test:
	python -m pytest -v

servers:
	python -c "import sys, runpy; sys.path.insert(0, 'src'); runpy.run_module('load_balancer.servers.run_servers', run_name='__main__')"
