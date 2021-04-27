from django.urls import path

from main.views import StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView

urlpatterns = [
    path('', StaffListView.as_view(), name='index'),
    path('create/', StaffCreateView.as_view(), name='create'),
    path('update/<int:pk>', StaffUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', StaffDeleteView.as_view(), name='delete')
]
