from django.urls import path
from .views import TreeView

urlpatterns = [
    path('trees/', TreeView.as_view(), name='tree_list'),
    path('trees/<int:id>', TreeView.as_view(), name='tree_process')
]