from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):

	perfil = Perfil()
	return render(request, 'perfil.html', {'perfil' :perfil, 'perfil_logado': get_perfil_logado(request)})




