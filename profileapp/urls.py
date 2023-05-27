
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("n/login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("n/register", views.register, name="register"),
    path("<str:username>", views.profile, name='profile'),
    path("n/following", views.following, name='following'),
    path("n/saved", views.saved, name="saved"),
    path("n/createpost", views.create_post, name="createpost"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:post_id>/comments", views.comment, name="comments"),
    path("n/post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/editpost", views.edit_post, name="editpost"),
    path("n/post/<int:post_id>/editprofile", views.Update_profile, name="editprofile"),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path ('Eprofile/', views.profile1, name="Eprofile"),
    path ('Update_profile/', views.Update_profile, name="Update_profile"),
    path('Company_Changepass/', views.comp_change_password, name='Company_Changepass'),
    path('Change_Password/', views.change_password, name='change_password'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path ('Searchbar/', views.searchbar, name="searchbar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
