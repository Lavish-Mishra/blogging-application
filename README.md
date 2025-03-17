# **Blogging Application** 

## Users can post their blogs on the web application and can interact with other user's blogs.



### **A user can do following things on the Web Application -**
> Post Blogs

> Modify own Blogs

> Delete own Blogs

> Comment on Blogs

> Like on Blogs
#

## Steps to  run this project
This site can be hosted on a server or local server and anyone connected to that server can access this blogging system through browser.



You can run this project on your system and that system can act as a server and devices connected to that same network as the system can also access that blog site.


**To run this project on your system follow these steps:**

1. Clone this project and go to the project folder.
2. Install python3.
3. Run this command on your terminal "pip install -r requirements.txt" this command will install all the required modules on your system.
   Note: Install pip modeule if not installed.
4. Now make changes in email_host_user and email_host_password according to you in "settings.py" file in project folder.
5. Now run following commands in your terminal in project folder
   1. python manage.py make migrations
   2. python manage.py migrate
   3. **python manage.py runserver <your-ip-address>**, or use **python manage.py runserver** to run it on localhost
   Note: to find your ip address run ipconfig command in yout terminal and also insert your ip address in allowed_hosts list in usersettings.py file if you are running server on your ip adddress.
6. Now you can access the site on the url it shows on command prompt.
#
## Superuser
You can manage your site on admin panel by going on url -->  <site-url>:8000/admin
Only superusers can access admin panel
you can create the superuser by running the command in command line
<<------  python manage.py createsuperuser    ----->>

All the user's password are written after hiphen(-) as username-password for the convenience.
You can view all other dumy usersnames after logging in as superuser in admin panel.

You can create new superuser by running the command in terminal:

**python manage.py createsuperuser**

and enter username, email, password for superuser.


Now login using superuser credentials and now you can manage your site.


