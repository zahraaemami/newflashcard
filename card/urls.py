
from django.urls import path , include
from card import views 
 
 
 
 
 
urlpatterns =[
    
    path('create/', views.CreateFlashCardView.as_view() , name = 'create_flash') ,

    path('update/<id>/' , views.UpdateFlashCardView.as_view() , name = 'Update_flash'), 

    path ('delete/<id>/' , views.DeleteFlashCardView.as_view() , name = 'delete_flash'), 

    path('list/<user_id>/' , views.ListFlashCardView.as_view() , name = 'list_flash') ,
]
