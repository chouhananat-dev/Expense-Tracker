from django.urls import path
from . import views
urlpatterns=[
    path('getexpense/',views.expense_list,name='expense_list'),
    path('addexpense/',views.add_expense,name='add_expense'),
    path('signup/',views.signup,name='sign_up'),
    path('',views.base,name='base_page'),
    path('delete/<int:pk>/',views.delete_expense,name='delete_expense'),
    path('edit/<int:pk>/',views.updateexpense,name='edit_expense'),
    path('export-csv/',views.export_expenses_csv,name='export_csv')
]