from django.urls import path
from . import views

urlpatterns = [
    path('',views.tweet_list,name="twet_list"),
    path('create',views.create_tweet,name="create_tweets"),
    path('<int:tweet_id>/edit/',views.tweet_edit,name="twet_edit"),
    path('<int:tweet_id>/delete/',views.tweet_delete,name="twet_delete"),
    path('registration/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('search/',views.text_search,name="tsearch"),
]