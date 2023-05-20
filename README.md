# Notes App
Using Django and Bootstrap


## Project Setup

1. Create virtual env using `python3 -m venv venv`
2. After activating virtual env, install django using `pip install django`
3. Change directory to root folder and perform DB migrations
```
    python manage.py makemigrations
    python manage.py migrate
```
4. Start server using `python manage.py runserver`

## Functionality

- Log in
    - via username & password
- Create an account
- Log out
- Add new note with Title, Description and Color
- Update Note
- Delete Note

## Screenshots

| Log In | Create an account | Home page |
| -------|--------------|-----------------|
| <img src="./screenshots/1.login.png" width="300"> | <img src="./screenshots/2.signup.png" width="300"> | <img src="./screenshots/3.home.png" width="300"> |

| Add Note | Modify Note | Note Modified |
| ---------------|------------------|-----------------|
| <img src="./screenshots/4.NoteAdded.png" width="300"> | <img src="./screenshots/5.ModificationPopup.png" width="300"> | <img src="./screenshots/6.Modified.png" width="300"> |

| Add Another Note | Delete Note | Note Deleted |
| ---------------|------------------|-----------------|
| <img src="./screenshots/7.Another.png" width="300"> | <img src="./screenshots/8.Delete.png" width="300"> | <img src="./screenshots/9.Deleted.png" width="300"> |
