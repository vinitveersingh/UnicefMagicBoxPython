Development Reference Notes: 

Part 1:
Install anaconda 
https://www.anaconda.com/download/

Part 2:
Setting Up Django Models
Note: Virtual enviroment are useful to test the project on different versions of dependency libraries

Step 1: Create a new python 3.5 along with other useful python libraries in a virtual enviroment called unicefenv
Command : conda create -n unicefenv python==3.5 anaconda

Step 2: Activate the virtual enviroment.(This is for windows. Some conda commands can vary for different OS )
Command: activate unicefenv

Step 3: Install a stable version of Django to the unicefenv
Command: pip install django==2.0.3

Step 4: Create a django project 
Command: django-admin startproject unicefproject

Step 5: Create an app inside the unicefproject
Commands: cd unicefproject(Go into the directory)
          python manage.py startapp magicbox
          
Step 6: Register the app in unicefproject settings.py file.
![image](https://user-images.githubusercontent.com/17389305/41102005-c2703736-6a33-11e8-94d8-bf83e7bb873f.png)

Step 7: Create models in the unicefproject/magicbox/models.py
Note: Models are database tables created using Django ORM
![image](https://user-images.githubusercontent.com/17389305/41102171-3d3c1926-6a34-11e8-986d-d87ad58fac48.png)

The above model can be roughly represented by the schema drawn below:
![image](https://user-images.githubusercontent.com/17389305/41102848-ceb8657a-6a35-11e8-9ea8-34e05d628e04.png)

Step 8: Register the model in unicefproject/magicbox/models.py
![image](https://user-images.githubusercontent.com/17389305/41102922-f5e96c0c-6a35-11e8-925a-c977e6662f32.png)

Step 9: Step back one folder and run the the following commands:
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

Steep 10: In order to see the tables we created we needs to start Django on the server and see it throught the admin file.
Before starting the server create a superuser.
Commands:
python manage.py createsuperuser
It will prompt you for a username and password. My username and passowrd are vinit and admin1234

Step 11: Start the server.
Commands: 
python manage.py runserver

Step 12: This will start running a virtual server running at 127.0.0.1:8000
![image](https://user-images.githubusercontent.com/17389305/41103377-00c79454-6a37-11e8-8f4f-909f0935904b.png)

Step 13: Now log on to you django admin to see the models that are created. Hit this URL : 127.0.0.1:8000/admin
Now you will be able to see the models you created.
Note: you will be required to log in with the super user details.
![image](https://user-images.githubusercontent.com/17389305/41103491-4af1e50c-6a37-11e8-91f1-15c70852ccc0.png)

Step 14: Now run the unicefproject/providerandcountryDB.py file to populate the ProviderandCountry database Table.
Command: python providerandcountryDB.py
In the admin panel an new entry will be created like this:
![image](https://user-images.githubusercontent.com/17389305/41103697-c7689270-6a37-11e8-9d7b-adc6325dc965.png)

Step 15: Now run the unicefproject/ColumbiaDB.py file to populate the CoulmbiaData database Table. This file uses pandas to read the csv file 
and populate the table accordingly.
Command: python ColumbiaDB.py 
In the admin panel an new entry will be created like this:
![image](https://user-images.githubusercontent.com/17389305/41103937-5277905a-6a38-11e8-8ae4-0c93f99bbb92.png)

Step 16: Now run the unicefproject/DRFDB.py file to populate the DRFData database Table.This file uses pandas to read the csv file 
and populate the table accordingly.
Command: python DRFDB.py 
In the admin panel an new entry will be created like this:
![image](https://user-images.githubusercontent.com/17389305/41103884-3568a1b6-6a38-11e8-8efc-64408d145cb8.png)
