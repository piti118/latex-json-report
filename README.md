# Latex Report Server

A flask blueprint based server that accepts json, render it on latex template and compile it and send back the pdf.

# Author
Piti Ongmongkolkul

# License

	Public Domain

# Requirements

* Python 3.5+ Need this for a sensible subprocess module. Not just 3 but 3.5.
* all other stuff in `requirements.txt`
* xelatex (Texlive should work in most cases)
	
# TLDR;

* first make sure you have python 3.5 and xelatex installed. Preferably using virtualenv or something along that line.
* `pip install -r requirements.txt`
* `python app.py`
* Point your browser to 
	* http://localhost:5000/basic/sample
	* http://localhost:5000/ultimate/sample
	* If you want to try this out with postman
		- Post {x: "aaa", y: "bbb"} to http://localhost:5000/basic


# Making a New Template

* See `templates/` for examples.
* The template engine is a customized jinja2. See `latex_jinja.py` for the full syntax.
	* Basic ones are
		* Variable `((( varname )))`
		* Block `((* for x in l *))`
* The format is copied from http://flask.pocoo.org/snippets/55/ . The choice is intended so that the template is self is a valid tex document so one can use latex editor to edit it.

# Making a New Blueprint

* use `blueprint.make_blueprint(name, templatemodule)`
* See app.py for example
	
# Helper

* To help develop the template the script test_template.py is provided. 
* The script will try to the template module provided and put it in tmp

# Docker
The docker file is provided. The tex-live there is a small one. A lot of package and fonts are not installed by default. If your file doesn't compile this might be the reason.

```
	docker run -p 5000:5000 .
```

# Todo

* make it a pypi package the only method needed to export is really `blueprint.make_blueprint`