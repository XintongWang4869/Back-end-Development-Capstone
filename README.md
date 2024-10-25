

**Environment Setup**

```
bash ./bin/setup.sh
exit
```

## Complete the Data Model Classes

Add properites with desired attributes to each model in "models.py"

To propagate the changes made to the models:    
* `python manage.py makemigrations`   
* `python manage.py migrate`

Check if you are ready to launch the application: `curl -s -o /dev/null -w "%{http_code}" http://localhost:8000`   
* -s: silent mode, meaning it won’t show progress or error messages.
* -o /dev/null: to discard the output by sending it to /dev/null, which is a special file that discards all data written to it.
* -w "%{http_code}": specifies a custom output format. 

## Fix Each Page 

1. Complete the URL in "urls.py"

> Django: Often uses **trailing slashes** in URL patterns to avoid unnecessary redirects.   
> * re_path():      
```
   urlpatterns = [
    re_path(r'^birthday/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.birthday_view),
]
``` 
> Flask: Does not require trailing slashes by default, but you can handle both versions explicitly.

2. Complete the view in `views.py`  

You can first use simple dictionary data to test functionality, which will be eventually replaced by deployed microservice url.