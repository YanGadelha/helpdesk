from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from helpdesk.models import OrdemServico
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()
def index_view(request):
    return render(request, 'helpdesk/index.html')

def login_view(request):
    error_message = None
    login_form = LoginForm()
    register_form = CustomUserCreationForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if 'login-form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                error_message = "Usuário ou senha inválidos"
                print(error_message)
        elif 'register-form' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('login')  
            else:
                print("Erros no formulário de registro:", register_form.errors)
                error_message = register_form.errors
    else:
        register_form = CustomUserCreationForm()

    context = {
        'login_form': login_form,
        'register_form': register_form,
        'show_register': False,
        'error_message': error_message,
    }
    return render(request, 'registration/login.html', context)

@login_required
def home_view(request):
    total_ordens = OrdemServico.objects.count()

    # Ordens por status
    status_counts = OrdemServico.objects.values('status').annotate(total=Count('status'))

    # Inicializar contadores
    ordens_pendentes = ordens_concluidas = ordens_nao_concluidas = 0

    # Atribuir os valores das contagens
    for status in status_counts:
        if status['status'] == 'aberto' or status['status'] == 'andamento':
            ordens_pendentes += status['total']
        elif status['status'] == 'concluido':
            ordens_concluidas = status['total']
        elif status['status'] == 'nao_concluido':
            ordens_nao_concluidas = status['total']

    return render(request, 'home/home.html', {
        'total_ordens': total_ordens,
        'ordens_pendentes': ordens_pendentes,
        'ordens_concluidas': ordens_concluidas,
        'ordens_nao_concluidas': ordens_nao_concluidas,
        'all_orders': OrdemServico.objects.all(),
    })

@login_required
def user_profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.full_name = request.POST.get('full_name')
        user.email = request.POST.get('email')
        user.birth_date = request.POST.get('birth_date')
        user.contact = request.POST.get('contact')
        user.company = request.POST.get('company')
        user.occupation = request.POST.get('occupation')
        user.sector = request.POST.get('sector')

        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))

        user.save()
        return redirect('home')

    context = {
        'user': user,
    }
    return render(request, 'home/home.html', context)

@login_required
def delete_user_view(request):
    user = request.user
    user.delete()
    return redirect('index')

@login_required
def add_order(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        urgency = request.POST.get('urgency')

        ordem_servico = OrdemServico(
            title=title,
            description=description,
            urgency=urgency,
            user=request.user  
        )
        ordem_servico.save()

        return redirect('home') 
    return render(request, 'home')

@login_required
def all_orders_view(request):
    print("Entrou na view") 
    all_orders = OrdemServico.objects.all()
    print(f"Total de ordens encontradas: {all_orders.count()}")
    print(f"Consulta SQL: {all_orders.query}")
    
    return render(request, 'home/home.html', {'all_orders': all_orders})

@login_required
def user_orders_view(request):
    user_orders = OrdemServico.objects.filter(user=request.user)
    return render(request, 'home', {'user_orders': user_orders})