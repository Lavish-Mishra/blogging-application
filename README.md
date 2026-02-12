# 📝 BlogSphere

> A full-stack **Blogging Web Application** built with **Django + SQLite + HTML/CSS**.  
> Users can register, create posts, like and comment on blogs — all in a clean and responsive interface.

---

![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=for-the-badge&logo=django)
![Backend](https://img.shields.io/badge/Backend-Python-blue?style=for-the-badge&logo=python)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%26%20CSS-orange?style=for-the-badge&logo=html5)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 🚀 Tech Stack

**Backend:** Django  
**Frontend:** HTML, CSS  
**Database:** SQLite  
**Authentication:** Django Built-in Authentication System  

---

## ✨ Features

- 🔐 User Registration & Login
- ✍️ Create, Edit & Delete Blog Posts
- ❤️ Like/Unlike Posts
- 💬 Comment System on Posts
- 👤 User-Specific Post Management
- 📰 View All Blogs Feed
- 🔎 Post Detail View
- 📱 Responsive Design
- 🚪 Secure Logout Flow

---

## ⚙️ Environment Variables

Create a `.env` file in your project root (optional but recommended):

```
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🧠 Installation

1. Clone the repository
```
git clone https://github.com/Lavish-Mishra/blogging-application.git
cd Blogging
```
2. Create Virtual Environment & Install Dependencies
```
python -m venv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate

pip install -r requirements.txt
```
3. Apply Migrations
```
python manage.py migrate
````

4. Run the Server
```
python manage.py runserver
``` 

## 🧰 Folder Structure
```
blogging-app/
│
├── blog/                  # Main blog app
│   ├── models.py          # Post, Comment models
│   ├── views.py           # Business logic
│   ├── urls.py            # App routes
│   ├── forms.py           # Django forms
│   └── templates/         # HTML templates
│
├── users/                 # User authentication app
│
├── static/                # CSS, images
│
├── manage.py
└── README.md
```

## 🧑‍💻 Author

Lavish Mishra

Backend Developer | Django & React Enthusiast
