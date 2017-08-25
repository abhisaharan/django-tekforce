# django-tekforce

Django project -  login and logout pages with signup options. "django.contrib.auth.forms" used for login and logout. 

awsebcli and pandas-datareader(includes pandas and numpy etc) installed. files for aws added like .ebextensions(inside django.config). This setting, WSGIPath, specifies the location of the WSGI script that Elastic Beanstalk uses to start your application.Also added requirements.text(pip freeze > requirements.txt) to let aws know what packages are installed.


Only compressed folder can be deployed in AWS. With every new version a new zip file of project is created.