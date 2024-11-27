# admin.py

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Администрирование сайта Listy"
    site_title = "Listy"
    index_title = "Добро пожаловать в панель управления"

admin_site = MyAdminSite(name='myadmin')
