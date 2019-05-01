from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import CadastrarUserForm

class CadastrarUsuario(View):
	
	template_name = 'cadastrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):

		#preenche o form
		form = CadastrarUserForm(request.POST)

		#verifica se e valido
		if form.is_valid():

			dados_form = form.data

			#cria o usuario
			usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

			#cria o perfil
			perfil = Perfil(nome=dados_form['nome'], sobrenome=dados_form['sobrenome'], 
				            nome_empresa=dados_form['nome_empresa'], telefone=dados_form['telefone'],
				            email=dados_form['email'], usuario=usuario)
			#grava no banco
			perfil.save()

			#redireciona para index
			return redirect('index')

	 	#se o form nao for valido devolve o form preenchido
		return render(request, self.template_name, {'form' : form})


		