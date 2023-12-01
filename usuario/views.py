'''
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
#permite trabja con formulario direcctamente
from django.views.generic.edit import FormView
from .forms import FormularioLogin


class LoginView(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio.html')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
'''