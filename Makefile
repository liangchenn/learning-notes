.PHONY: all find_nb render_html clean
 variables
path ?= .

all:
	@echo "path= $(path)"

find_nb:
	@find $(path) -name *.ipynb 

render_html:
	@find $(path) -name *.ipynb -exec jupyter nbconvert --to html {} \;

clean:
	@find $(path) -name .ipynb_checkpoints -exec rm -rf {} +
