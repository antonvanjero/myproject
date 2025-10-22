from django.urls import path
from . import views
urlpatterns=[
    path("", views.index1, name='index1'),
    path('contact/',views.contact_view,name='contact'),
    path('contact/success',views.contact_success,name='contact_success'),
    path('demo/',views.demo,name='demo'),
    path('sample/',views.sample,name='sample'),
    path('hello/',views.new_page),
    path('students/',views.students,name='students'),
    path('arrays/',views.arrays,name='arrays'),
    path('form/',views.reg_form,name='form'),
    path('add/',views.add_student,name='add student'),
    path('update/',views.update_student),
    path('delete/',views.delete_student),
    path('student_data/',views.student_data),
    path('blog/',views.blog,name='blog'),
    path('blog1/<int:blog_id>/',views.blog1,name='blog1'),
    #path('product/',views.product_list,name='product_list'),
    path('add_product/',views.add_product),
    path('email/',views.send_email_view),
    path('upload/',views.upload_file, name='upload_file'),

    path("index/", views.index, name="index"), 
    path("get-data/", views.get_data, name="get_data"), 
    
    path('storage_demo/', views.storage_demo, name='storage_demo'), 

    path('set_cookie/', views.set_cookie_view), 
    path('get_cookie/', views.get_cookie_view), 
    path('delete_cookie/', views.delete_cookie_view), 

]