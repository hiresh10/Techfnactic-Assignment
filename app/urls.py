from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('home/',views.Home, name='home'),
    path('signuppage/',views.SignupPage,name='signuppage'),
    path('register/',views.Register,name="register"),
    path('loginpage/',views.LoginPage,name='loginpage'),
    path('login/',views.LoginUser,name="login"),
    path('contactpage/',views.ContactPage,name='contactpage'),
    path('contact/<int:pk>',views.Contact,name="contact"),
    path('productpage/',views.Product_page,name='productpage'),
    path('add/<int:pk>',views.Add_product,name='add'),
    path('updatepage/',views.Update_page,name="updatepage"),
    path('update/<int:pk>',views.update_image,name="update"),
    path("logout/",views.logout,name="logout"),

######################---Admin Url---#########################

    path('adminloginpage/',views.Admin_loginpgae,name="adminloginpage"),
    path('adminhome/',views.Admin_home,name="adminhome"),
    path('adminlogin/',views.Aminlogin,name='adminlogin'),
    path('delete/<int:pk>',views.UserDelete,name='delete'),
    path('productcards/',views.Product_cards,name="productcard"),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path("adminlogout/",views.adminlogout,name="adminlogout"),



]
