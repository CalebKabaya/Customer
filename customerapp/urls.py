from django.urls import re_path,include
from .views import CustomersViewSet,CardViewSet,AccountViewSet
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'customer',CustomersViewSet,basename='Customer')
router.register(r'account',AccountViewSet,basename='Account')
router.register(r'cards',CardViewSet,basename='Cards')


urlpatterns=[
    re_path('api/', include(router.urls), name='api'),
    re_path('^$',views.customers, name='customers'),
    re_path('addcustomers/',views.addcustomer, name='addcustomers'),
    re_path(r'^viewcustomer/(?P<customer_id>\d+)?$', views.viewcustomer, name='viewcustomer'),
    re_path(r'^delete/(?P<cust_id>\d+)?$', views.delete, name='delete_cust'),
 


    # path('api/account/', views.Account.as_view(), name="accounts"),

    # re_path('^$',views.welcome,name = 'welcome'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)