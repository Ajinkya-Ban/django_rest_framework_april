Django Rest framewrok
-------------------------------------------
Q. What is mean by Django?
------------------------------------------------------
1. Django is open source web framework. It is wriiten in python and its known for simplicity.
2. It follows "batteries-included" philosphy.
3. This includes componantes like handling the database, handling the urls, creating the templates etc.


Q. What is mean by API?
------------------------------------------------------
1. API is acronym for Application programming Interface. 
2. Two machines use it to communicate with each other.
3. An API is used by two applications trying to communicate with each other over a network or Internet.
4. The API acts as mediator between Django and other application.
5. Other applications like Andriod phone, ios phone, web browsers.
6. The main task of API is to receive data from applications and provide them to the backend. This data
	usually in the form json.


Q. What is mean by Rest API?
------------------------------------------------------
1. REST stands for "Reprentaional State Transfer".
2. REST is architecture on which we develop web services. 
3. Web Services can be understood as your device connects to the internet.
4. When you search for anything on google or watch something on youtube, These are web services where
	your device is communicating to a server.
5. When these web services use REST architecture then it is called RESTful Web Services.
6. These web services use HTTP to transmit data between machines. 

*Following are the important key REST API request method*
----------------------------------------------------------------------------------
1. GET : It display the data from database to front-end 
2. POST : It create a new data or records.
3. PUT : It update the records
4. PATCH : It is called partial update. Only update single field.
5. DELETE : It will delete the data from database.

Q. What is mean by RESTful API?
---------------------------------------------------------
1. A RESTful API acts as a translator between two machines communicating over a web service.
2. This is just like an API but its working on RESTful Web Service. 
3. Web developers program REST API such that server can receive the data from application. These
	applications can be web app,Andriod/iOS ap etc..
4. RESTful API's today return JSON files which can be interpreted by a different devices.

Q. What is mean by Django Rest framework?
------------------------------------------------------------
- 


Q. What is mean serilization DRF?
--------------------------------------------------------------
Serialization in Django is the process of converting complex data types, such as Django model instances, 
into formats that can be easily rendered, transmitted, or stored, such as JSON or XML. 
The reverse process, deserialization, involves converting data from these formats back into Django 
objects.

Use Cases of Serialization
=========================
1. API Responses: Converting model data into JSON for APIs (e.g., Django REST Framework).
2. Data Export: Exporting data in a specific format, such as JSON or XML.
3. Data Storage: Saving the state of objects in a format that can be retrieved later.

For more advanced use cases, like building RESTful APIs, Django REST Framework (DRF) provides 
a serializers module.



Q. How we can setup DRF using django?
-------------------------------------------------------------
Note : We use postman tool to check the API's.

1. Go to this website https://www.django-rest-framework.org/
2. Open the pycharm editor and create a project provide any name.
3. After creating the project install the packages like django and djangorestframework, by using following
	commands,
	a) pip install django
	b) pip install djangorestframework
4. After installing the packages create a django project using the command as below,
	django-adimn startproject projectname
5. After creating the project go to created project and create the app using the command as below,
	python manage.py startapp myapp
6. After creating project and app create the database using mysql.
7. After creating the database go to the settings.py file and register the app and DRF by using following
	names.
	a) 'myapp'
	b) 'rest_framework',
	
8. Add the database related configurations in settings.py file as below.
	
	DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mydb',
		'USER': 'root',
		'PASSWORD': 'admin',
		'HOST':'localhost',
		'PORT':'3306',
	}
}

9. After adding the database configurations run the two commands, before using this command make sure
	you install mysqlclient library, it not then use pip install mysqlclient
	
	1. python manage.py makemigrations
	2. python manage.py migrates


10. After using above commands create the superuser by using the command as below,
	python manage.py createsuperuser
	
11. After executing all the steps run the server using the command 
	  python manage.py runserver
	  
12. If we want to log in with admin then use the url like http://127.0.0.1:8000/admin and provide the
	  username and password.
	 
13. Create the simle model as you like in models.py file.
14. Register the created model in admin.py file.
15. Then run the makemigrations and migrate command.
16. Create the one python file name as serializers.py in myapp folder.
=========================================================================

Django REST Framework (DRF), generics:
----------------------------------------------------------
In Django REST Framework (DRF), generics are a set of pre-defined views that provide a streamlined 
way to handle common API operations such as creating, retrieving, updating, and deleting resources. 
These views are built on top of DRF's class-based views and  combine functionality like serializers, 
querysets, and request handling into reusable components.

Why Use Generic Views?
==========================

Simplicity: Reduce boilerplate code for CRUD operations.
Flexibility: Customize behavior by overriding methods.
Scalability: Combine with DRF's serializers and authentication mechanisms.

Types of Generic Views
=======================
1. ListAPIView : Used for fetching a list of objects.
2. RetrieveAPIView : Used for fetching a single object by its ID or some unique identifier.
3. CreateAPIView: Used for creating a new object.
4. UpdateAPIView : Used for updating an existing object.
5. DestroyAPIView : Used for deleting an object.
6. ListCreateAPIView: Combines ListAPIView and CreateAPIView to allow listing and 
    creating resources.
7. RetrieveUpdateDestroyAPIView:Combines RetrieveAPIView, UpdateAPIView, and DestroyAPIView 
	for a single resource.

When to Use Generics?
===========================
1. For Standard CRUD Operations: Generics are perfect for straightforward operations.
2. For DRY (Don't Repeat Yourself) Code: They prevent repeating the same logic in multiple views.


Authentication and permissions
==========================
- In django rest framework authentication and permission are key componanets for controlling access
  to API endpoints.
  
1. Authentication:
	------------------------
	- Authentication is the process of identitfying the user making the request.
	- DRF provides built-in authentication classes and allow custom implementation.
	
Common Authentication classes:
-----------------------------------------------
a) BasicAuthentication: Uses HTTP basic authentication(username and password).
b) SessionAuthentication: We use django's session framework.
c) TokenAuthentication: Uses token for stateless authentication.
d) JWTAuthentication: Uses JSON Web Token for secure authentication via third party library like
	djangorestframework-simplejwt.
	

2. Permission:
	----------------------
	- Permissions determine wether the authenticated user can access specific views or action.
	- DRF comes with built in permissions and supports custome permissions.
	
Common Permission classes:
----------------------------------------
a) AllowAny : Allows unrestricted access.
b) IsAuthenticated : Restricts access to authenticated users.
c) IsAdminUser : Only access admin which is created using createsuperuser command.
d) IsAuthenticatedOrReadOnly : Allows authenticated users full access but unauthenticated users can
	only read.

=================================================================================
Token Authentication:
-------------------------------
- Token authentication in Django Rest Framework allows you to secure your api's by requiring clients
   to authenticate using tokens.

Steps to perform token Authenticaton:
----------------------------------------------------
1. In settings.py we add below code
	REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]

}

2. In settings.py add 'rest_framework.authtoken' in installed_app section.
3. Stop the server and run the command python manage.py migrate. This command creates the table 
    which store the tokens against the user.
4. Run the server and go to admin panel, you will see one model name as Token. 
5. Create some users and provide them token.

Postman steps to perform token authentication:
-------------------------------------------------------------------
1. Select the http method like GET/POST, then put the url.
2. Go to header section of postman then put the values like,
	a) key --> Authorization
	b) value ---> Copy the token from admin panel of users.
3. Hit the url and check the responses.
4. Check also without passing token, what response you will get.
