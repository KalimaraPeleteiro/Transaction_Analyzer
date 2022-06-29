<h1 align="center"> MoneyAnalyzer </h1>

A server-side web app that allows the user to upload a list of financial transactions, giving feedback over potential frauds and illicit movements.
<br></br>
![report](https://user-images.githubusercontent.com/94702837/176440028-bf4740d7-4653-4253-bddd-fb9a6dc67796.png)

## 👨‍💻 Technologies
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" width=50 height=50/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width=50 height=50/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain.svg" width=50 height=50/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain-wordmark.svg" width=50 height=50/>

<br></br>
## 🚀 Project
The website was made using a modified free template (_template.zip_), that is inside the project folder. 
It has a few key functionalities, such as:
- Login/SignUp system, with encrypted passwords.
- Suport to CSV files with transactions, that are stored in your account.
- A report over suspicious transactions, showing separating them from others.

  ### 🔃 Login/Signup System
  To register into the app, the user will need offer only two things: a username and his email. After the appropriate verifications are made,
  a six-digit password encrypted with the BCrypt algorithm is sent to their email. The user can then use this password to enter the app.
  <br></br>
  ![login](https://user-images.githubusercontent.com/94702837/176452346-41c0e2a7-e53b-4a2c-b13c-a46624ef35d3.png)
  ![register](https://user-images.githubusercontent.com/94702837/176452368-a85a2a8a-6832-4fe6-8879-b55f8ba02843.png)

  
  ### 💼 Import Rules
  The app won't accept any CSV file. The file (that should be generated by a third-party) must contain eight key values:
  - The bank from which the transaction was made
  - The agency from which the transaction was made
  - The account number from which the transaction was made
  - The bank for which the transaction was
  - The account for which the transaction was
  - The account number for which the transaction was
  - The value of the transfer
  - The date and hour the transfer was made
  
  It'll be rejected any transactions that don't have one of these info. Besides that, the app will only read transactions from the same day at a time,
  therefore, any other records of transactions that ocurred in other date besides the first one in the CSV file will be ignored. In summary, the users should
  import their daily transactions at a time instead of grouping them all together and sending a bunch of them.
  <br></br>
  The user will have acess to all transactions imported into the app, with an additional button showing all the details.
  <br></br>
  ![import](https://user-images.githubusercontent.com/94702837/176452446-03a4f33f-06d9-4d2a-a14b-954a847e09f4.png)
  ![history](https://user-images.githubusercontent.com/94702837/176452468-709e8a46-f30e-422b-b05f-3552cedddde3.png)
  ![detail](https://user-images.githubusercontent.com/94702837/176452474-e25497dd-6d2f-4741-b6d6-d89b91ffb724.png)
  
  ### 💸 Suspicious Transactions
  Right now, the transactions labeled as "suspicious" are the ones with value over 10000. There are plans to change this, however, adding a more
  "detailed" analysis. I'm looking to build a ML model capable of analysing such values and identyfing potential suspicious transactions. This is a
  work in progress, though, and therefore some time will be needed for this.
  
<br></br>
## 💻 Downloading the Project
If you wish to download the files and see the project working by yourself, a few steps are going to be needed.
You need to make sure that you have Python installed, such as some few libraries, that will be listed down below.
```
# Libraries used in the project
Django==4.0.5
psycopg2-binary==2.9.3
bcrypt==3.2.2
```
> It's of major importance that you only download such libraries _after_ inside the virtual environment. To enter the venv, use the code 
> `source "path-to-venv/venv/bin/activate"`. After that, you can simply install the libraries using commands such as `pip install django==4.0.5`.

With the libraries installed you will also need two other things. The first one is PostgreSQL, and the second one is to modify, in _MoneyAnalyzer/settings.py_
the database configurations to fit your created database. The final setting should be something close to this.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DatabaseName',
        'USER': 'UserName',
        'PASSWORD': 'UserPassword',
        'HOST': 'localhost'
    }
}
```
After the database is configured, use the commands `python manage.py makemigrations` and `python manage.py migrate` to create the needed tables
in your database.
With this out of the way, you can build the server with `python manage.py runserver`. The app will be available in http://127.0.0.1:8000.

## 🙇‍♂️ Any Suggestions?
In case of any suggestions, opinions or criticism, please, contact me. I'm looking forward to keeping improving always, and feedback
is always precious.