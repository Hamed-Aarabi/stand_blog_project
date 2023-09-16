from django.shortcuts import redirect
from django.contrib import messages
class MyLoginRequiredMIxin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must Login to see article details.')
            return redirect('accounts:login')
        return super(MyLoginRequiredMIxin, self).dispatch(request, *args, **kwargs)



