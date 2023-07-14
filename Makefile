# variables
path ?= .

all:
	@echo "path= $(path)"

find_html:
	@find $(path) -name *.ipynb 

render_html:
	@find $(path) -name *.ipynb -exec jupyter nbconvert --to html {} \;
