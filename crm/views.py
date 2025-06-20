from django.shortcuts import render
from account_manager.decorators import allowed_users

@allowed_users(allowed_roles=['admin'])
def index(request):
    return render(request, 'crm_templates/index.html')
