# CRM (Django/Vue.js)

This is a simple CRM (customer relationship management). Here users can register leads with different statuses and other important information.
There are different roles, so a manager should be able to add users which a normal user shouldn't.
For the backend, I used Django Rest Framework to set up the API endpoints.
Authentication and tokens are mede with Djoser.


# Stack

![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/Vue%20js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![image](https://img.shields.io/badge/Bulma-00D1B2?style=for-the-badge&logo=Bulma&logoColor=white)



# How to run locally

## To run frontend (inside frontend directory):
### Project setup
```
npm install
```
### Compiles and hot-reloads for development
```
npm run serve
```

## To run backend (inside backend directory):
### Project setup
```
pip install -r requirements.txt
```
### Run development server
```
python manage.py runserver
```
