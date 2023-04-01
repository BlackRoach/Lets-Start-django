from django.urls import path

from accountapp.views import hello_world

# 추후 라우팅 시 주소를 간단하게 바꿀 수 있음 ex) accountapp:hello_world
app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]