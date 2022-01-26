from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("todo/create/", views.create_todo, name="create_todo"),
    path("todo/delete/<uuid:todo_id>", views.delete_todo, name="delete_todo"),
    path("todo/edit/<uuid:todo_id>", views.edit_todo, name="edit_todo"),
    # path('admin/', admin.site.urls),
]
