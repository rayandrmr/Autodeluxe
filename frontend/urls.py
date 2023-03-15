from django.urls import path
from frontend import views
urlpatterns=[
    path('home/', views.homepage, name="home"),
    path('single/<int:dataid>/', views.single, name="single"),
    path('aboutf/',views.aboutf,name="aboutf"),
    path('cars/', views.cars, name="cars"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('loginpag/', views.loginpag, name="loginpag"),
    path('saveuserlogin/', views.saveuserlogin, name="saveuserlogin"),
    path('custemerlogin/', views.custemerlogin, name="custemerlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('saveadcheckout/', views.saveadcheckout, name="saveadcheckout"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct")

]



