from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

class CustomAdminSite(admin.AdminSite):
    site_header: str = "DeepInSex Administration Panel"
    site_title: str = "DeepInSex Admin"

class CustomAdminConfig(AdminConfig):
    default_site: str = "deepinsex.custom_admin.CustomAdminSite"