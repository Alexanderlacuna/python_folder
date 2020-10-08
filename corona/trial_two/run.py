from jinja2 import Environment,PackageLoader,select_autoescape

env=Environment(

	loader=PackageLoader("trial_two",'templates'),
	autoescape=select_autoescape(["html","xml"])
	)



template=env.get_template("root.html")
print(template.render(summmary="testing jinja2"))