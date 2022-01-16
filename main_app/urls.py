from django.urls import path
from . import views


urlpatterns = [ 
    path("", views.home_page, name="home_page"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path("delete-todo/<int:todo_id>", views.delete_todo, name="delete_todo"),
    path("edit/<int:todo_id>", views.edit_todo, name="edit_todo"),
    # path('admin/', admin.site.urls),
]
