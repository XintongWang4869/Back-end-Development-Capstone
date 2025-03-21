# A Band Website using Django

This project is to build a band management platform utilizing a hybrid Django-Flask architecture.

This is the core Django application that handles concert scheduling and user authentication. It is integrated with two Flask microservices: a [song management service](https://github.com/XintongWang4869/Back-End-Development-Songs) that supports CRUD operations with MongoDB, and an [image management service](https://github.com/XintongWang4869/Back-End-Development-Pictures) that provides RESTful APIs.

## Demo

Users will be able to perform the following actions on the site:

Anonymous use cases:
* The user visits the Django Website home page.
<img src="./static/images/homepage.png" alt="homepage" width="400"/>

* The Song page shows songs and lyrics.
  
* The Picture page shows pictures from past concerts.
<img src="./static/images/photos.png" alt="photos" width="400"/>

* The user can sign into the application.
<img src="./static/images/login.png" alt="login" width="400"/>

Signed in use cases:
* The user can see their concerts.
* The user can book a concert.
* The user can delete their reservation.
<img src="./static/images/concerts.png" alt="concerts" width="400"/>  

Admin use cases:
* Admin can change the concert date.

<br>


## Lab

**Environment Setup**

```
bash ./bin/setup.sh
exit
```

### Complete the Data Model Classes

Add properties with desired attributes to each model in "models.py"

To propagate the changes made to the models:    
* `python manage.py makemigrations`   
* `python manage.py migrate`

Check if you are ready to launch the application: `curl -s -o /dev/null -w "%{http_code}" http://localhost:8000`   
* -s: silent mode, meaning it won’t show progress or error messages.
* -o /dev/null: to discard the output by sending it to /dev/null, which is a special file that discards all data written to it.
* -w "%{http_code}": specifies a custom output format. 

### Fix Each Page 

1. Complete the URL in "urls.py"

> Django: Often uses **trailing slashes** in URL patterns to avoid unnecessary redirects.   
> * Additional tips on re_path():      
>   ```
>      urlpatterns = [
>       re_path(r'^birthday/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.birthday_view),
>   ]
>   ``` 
> Flask: Does not require trailing slashes by default, but you can handle both versions explicitly.

2. Complete the view in "views.py"  

You can first use simple dictionary data to test functionality, which will be eventually replaced by the deployed microservice URL.

### Admin

Superuser: `python3 manage.py createsuperuser`

## Deploy on IBM Kubernetes Services

1. Setup the environment
2. Replace with deployed microservice URLs.
3. Make migrations
4. Check if the app can run locally: `python3 manage.py runserver`
5. Create a Dockerfile
6. Build and push the image
7. Create a deployment.yml
8. `kubectl apply -f ./deployment.yml`  
> Watch the pods: `kubectl get pods -w`

9. Access the deployment from outside the cluster: `kubectl port-forward po/pod_id 8000:8000`
