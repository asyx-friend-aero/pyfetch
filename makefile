DOAS := $(shell which doas 2>/dev/null || which sudo 2>/dev/null || echo "echo 'No doas/sudo found';")

build:
	nuitka pyfetch.py -o pyfetch

install:
	$(DOAS) cp pyfetch /usr/local/bin/pyfetch
	$(DOAS) chmod +x /usr/local/bin/pyfetch
