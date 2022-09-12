from django.urls import path

from blog.views import (
  index,
  signup,
  signin,
  logout,
  settings,
  upload,
)

urlpatterns = [
  path('', index, name='index'),
  path('settings', settings, name='settings'),
  path('upload', upload, name='upload'),
  path('signup', signup, name='signup'),
  path('signin', signin, name='signin'),
  path('logout', logout, name='logout'),
]