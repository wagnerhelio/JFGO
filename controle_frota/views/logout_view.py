from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def logout_view(request):
    logout(request)
    list(messages.get_messages(request))
    return redirect('login')
