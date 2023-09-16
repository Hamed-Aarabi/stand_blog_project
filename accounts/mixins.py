from django.shortcuts import redirect


class MyAuthebticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.email:
            return redirect('home:home')
        return super(MyAuthebticatedMixin, self).dispatch(request, *args, **kwargs)