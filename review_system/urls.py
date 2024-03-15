from django.urls import path
from review_system import views

urlpatterns = [
    path("", views.get_all_reviews, name="reviews_list"),
    path("register/", views.create_user, name="create_user"),
    path("log_in/", views.login_form, name="login_form"),
    path("write_review/", views.write_review, name="review_form")
]