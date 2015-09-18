from django.conf.urls import include, url
from django.contrib import admin
from emi import views

urlpatterns = [
		url(r'^admin/', include(admin.site.urls)),
		url(r'^main/',views.emi_main,name='emi_main'),
		url(r'^mains/',views.emi_calc,name='emi_calc'),
		url(r'^error/',views.emi_calc,name='emi_calc'),
]
    
