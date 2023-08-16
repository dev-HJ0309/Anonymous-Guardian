from django.urls import path
from django.views.generic import TemplateView

app_name = 'member'



urlpatterns = [
    path('', TemplateView.as_view(template_name='mypage/test.html'), name='success'),
 ]

