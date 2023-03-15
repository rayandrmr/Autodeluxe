from django.urls import path
from backapp import views


urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('admin/',views.admin,name="admin"),
    path('saveadminpage/',views.saveadminpage,name="saveadminpage"),
    path('category/',views.category,name="category"),
    path('savecategorypage/',views.savecategorypage,name="savecategorypage"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategorypage/<int:dataid>',views.updatecategorypage,name="updatecategorypage"),
    path('deletecategory/<int:dataid>',views.deletecategory,name="deletecategory"),
    path('products/', views.products, name="products"),
    path('saveproducts/', views.saveproducts, name="saveproducts"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),
    path('displayorder/',views.displayorder,name="displayorder")


]