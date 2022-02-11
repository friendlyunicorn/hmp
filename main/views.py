from django.shortcuts import render
from users.models import Profile


def main_index(request):
    if request.user.is_anonymous:
        user = None
    else:
        user = Profile.objects.get(user=request.user.pk)

    data = {
        'user': user
    }
    return render(request, 'main/index.html', data)