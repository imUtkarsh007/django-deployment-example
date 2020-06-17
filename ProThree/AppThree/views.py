from django.shortcuts import render
from AppThree.models import User
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'AppThree/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'AppThree/users.html',context=user_dict)
