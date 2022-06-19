from members.models import User

from members.models import complaint

def create_email(request):
    user = request.POST.get('username')