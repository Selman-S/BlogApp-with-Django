from django.urls import path

from blog.views import (
  index,
  signup,
  signin,
  logout,
  settings,
  upload,
  like_post,
)

urlpatterns = [
  path('', index, name='index'),
  path('settings', settings, name='settings'),
  path('like_post', like_post, name='like_post'),
  path('upload', upload, name='upload'),
  path('signup', signup, name='signup'),
  path('signin', signin, name='signin'),
  path('logout', logout, name='logout'),
]