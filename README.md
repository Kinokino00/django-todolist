# Todolist

### 建立虛擬環境

- pip install pipenv
- pipenv shell

### 安裝套件

- pipenv install django

### 產生專案

- django-admin startproject todolist .
  - . =>本地產生需要的目錄跟檔案

### 啟動 Server

- python manage.py runserver

### 同步資料庫

- python manage.py makemigrations
- python manage.py migrate

### 建立超級使用者

- python manage.py createsuperuser
