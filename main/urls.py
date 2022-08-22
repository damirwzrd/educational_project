from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index_page', views.index_page, name='index_page'),
    path('login', views.login_page, name='login_page'),
    path('courses', views.courses_page, name='courses_page'),
    path('results', views.results_page, name='results_page'),
    path('course_detail/<int:pk>', views.course_detail_page, name='course_detail_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)