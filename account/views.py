from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login, authenticate
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import SignUpForm, LoginForm
from .models import User
from django.views.generic import TemplateView ,ListView, DetailView, CreateView, DeleteView
from .serializers import UserListSerializer

# class UserListView(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('date_joined')
#     serializer_class = UserListSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     def list(self, request, *args, **kwargs):
#         users = self.queryset
#         return render(request, 'dashboard.html', {'users': users})

class DashboardView(TemplateView):
    template_name = '_admin/index.html'
    
    
    
class UserListView(ListView):
    model = User
    template_name = '_admin/users-list.html'
    
    # def get_success_url(self):
    #     return reverse("user-detail.html")
    
class UserDetailView(DetailView):
    model = User
    template_name = '_admin/user-detail.html'
       
    
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users-list')  # Replace 'home' with your home URL
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
