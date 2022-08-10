from django.shortcuts import render,redirect,reverse
from .models import Filme,Usuario
from django.views.generic import TemplateView,ListView,DetailView,FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarUsuarioForm,HomepageForm

# Create your views here.

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = HomepageForm
    def get_success_url(self):
        email=self.request.POST.get("email")
        lista_usuario=Usuario.objects.filter(email=email)
        if lista_usuario:
            return reverse("filme:login")
        else:
            return reverse("filme:criarconta")
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        else:
            return super().get( request, *args, **kwargs)

class Homefilmes(LoginRequiredMixin,ListView):
    template_name = "homefilmes.html"
    model = Filme

class Detalhesfilme(LoginRequiredMixin,DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self,request,*args,**kwargs):
        filme=self.get_object()
        filme.visualizacoes+=1
        filme.save()
        usuario=request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme,self).get_context_data(**kwargs)
        lista_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["lista_relacionados"] = lista_relacionados
        return context

class Pesquisa(LoginRequiredMixin,ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa=self.request.GET.get("query")
        object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
        return object_list

class Editarperfil(LoginRequiredMixin,UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ["first_name","last_name","email"]
    def get_success_url(self):
        return reverse("filme:homefilmes")

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarUsuarioForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')

"""def homepage(request):
    return render(request, "homepage.html")

def homefilmes(request):
    context={}
    lista_filmes=Filme.objects.all()
    context["lista_filmes"]=lista_filmes
    return render(request, "homefilmes.html",context)"""