# Dacodes API

# General overview:

This application was created for e-learning purposes and we will have, as professors, the chance to manage courses, lessons, questions and students subscriptions to them, while
as students we can use the UI to get an account, login to the system and access to the platform resources.

# Design Pattern:
- MVC (MTC)

# Languages, Frameworks and Libraries 
- Python3.8 / Django3.0: Used as main language and framework respectively.
- Djangorestframework 3.11: Used to create and manage our API rest, endpoints and database.
- Djangorestframework-simple JWT 4.4: Used to implement JWT validation to give access security to our APIrest.  
- Pytest 6.0: Used to write some unittest and get coverage metrics for our APIrest and application models.
- Coreapi 2.3: Used for generate useful documentation for the front end team.
 
# User Roles:
- Students(users)
- Professors(admin) 

# Modules:
- Courses
- Lessons
- Questions
- Users
- Admin

#Install instructions:

Before running please follow this steps:

- 1- Create new folder in your selected path(Desktop, Downloads, Documents, etc..)
- 2- Clone this repository and move the unzipped folder to the new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command (MacOS):
```
                            python3 -m venv <yourvenvname>
```    

# Running local Dacodes API  

- 1- Open your cloned repository (located in your new folder created in previous section) using
     your code editor preferred (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one folder back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment, return to your cloned repository (this should be one up folder) using "cd <reponame>" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```
- 6- Done!!! You can run your local server using the nex command (MacOS):
```
                            python3 manage.py runserver
```
- 7- Open your browser at **127.0.0.1:8000**

# Instructions for Dacodes API use

# Student user:

- 1- Once you are running your local server (**127.0.0.1:8000**) in your browser, you will get the student login form. 
As first time use, you will need to have a student account and you can create it in the Sign up here link. 
Note: You can create a new one or you can access with follow credentials:
Username:TestUser
Password:testuser1234

- 2- Once you login to the system, you can access to the courses, lessons and his respective form questions.

- 3- You can logout at any moment using the logout navbar button

# Professor(Admin) user:

- To get access as Professor and manage the APIrest resources you will need to create a superuser account. This is very important because otherwise
the JWT system won't be let you access to the APIendpoints, create and/or get data and access to API documentation so please before try to use it, follow
the next steps:

- 1- On your code editor's terminal type the next command(MacOS) and follow the prompt instructions:
```
                            python3 manage.py createsuperuser
```  
- 2- DONE!!, Once you have created a superuser go to the next url and access with your superuser credentials
- **http://127.0.0.1:8000/admin/**
Now you can access to admin module's dashboard

- In your admin dashboard you will have access to our API main resources and you will have the chance to manage, create, modify and delete content
for student users

# API endpoints

- Once you are logged as Professor(Admin) in the system, you will have access to our APIrest endpoints:
    - Modules endpoints:
        - **http://127.0.0.1:8000/api/v1/courses/** 
        - **http://127.0.0.1:8000/api/v1/lessons/**
        - **http://127.0.0.1:8000/api/v1/questions/** 
        
    - Additional action decorators:
        - **http://127.0.0.1:8000/api/v1/courses/{id}/students/**
        - **http://127.0.0.1:8000/api/v1/courses/{id}/lessons/**
        - **http://127.0.0.1:8000/api/v1/lessons/{id}/students/**
        - **http://127.0.0.1:8000/api/v1/lessons/{id}/questions/**
        
        
# Additional features

- Our API have some unit tests to verify and detect possible bugs. As we mentioned before, we used pytest library and you can run these tests
  following the next steps:
  
  - Location path API tests:
                        - DacodesApi/core/tests.py
                        
  1- On your code editor's terminal type the nex command:
```
                            pytest core/tests.py
```           
  - Location path Models tests:
                        - DacodesApi/courses/tests.py 
                        - DacodesApi/lessons/tests.py
                        - DacodesApi/questions/tests.py 
                        
  2- On your code editor's terminal type the desired  next command:         
 
 ```
                            pytest courses/tests.py
                            pytest lessons/tests.py
                            pytest questions/tests.py
``` 
- With this function you will have a unit test detail report for our API and his different modules coverage percentage.  
 
#Documentation url

- This will be a very useful guide about our APIendpoints for its FrontEnd team implementation
- NOTE: Remember to be logged as Admin! 
                                                - **http://127.0.0.1:8000/documentation/**
