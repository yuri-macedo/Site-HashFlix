<h1 align="center">
    <img alt="HashFlix" Title="HashFlix" src="/static/images/hashflix.png">
</h1>

<p align="center">
    •<a href="#Descrição">  Descrição </a>
    •<a href="#Funcionalidades">  Funcionalidades </a>
</p>
 	
 <h2 id="Descrição">
     Descrição
 </h2>
 
 <p style="text-align:justify" >
     Esse projeto possui como objetivo criar um site que seja uma replica da Netflix, utiizando os conhecimentos de programação em Python, o framework Django, a linguagem de marcação HTML e CSS. 
 </p>

 <h2 id="Funcionalidades">
     Funcionalidades
 </h2>
 
 O projeto foi desenvolvido com as seguintes funcionalidades: 
 
 <h3>
     Criar Conta
 </h3>
 
 Para a criação da conta foi utilizada o formulário e o modelo de usuário do Django, salvando as informações no banco de dados SQLite3.
 
<h1 align="center">
    <img src="/Gifs/CriarConta.gif">
</h1>

 <h3>
     Login
 </h3>
 
 Para a realização do login foi utilizada novamente o formulário e o modelo de usuário do Django, consultando as informações no banco de dados SQLite3.
 
<h1 align="center">
    <img src="/Gifs/Login.gif">
</h1>

 <h3>
     Filmes Novos, Em Alta e Assistidos Recentemente
 </h3>
 
 Os filmes/séries são exibidos pelos mais recentes, em alta e assistidos recentementes, de acordo com as informações salvas no banco de dados SQLite3, verificando o modelo do filme e do usuário que está logado no momento.
 
<h1 align="center">
    <img src="/Gifs/Homefilmes.gif">
</h1>

 <h3>
     Detalhes do Filme
 </h3>
 
 Cada filme possui uma página onde é possível verificar os episódios, onde o episódio é um modelo que possui relação de muitos para um com o modelo de filme. Assim, são exibidos os episódios que são daquele filme/série e também os outros filmes/séries relacionados ao filme, com base na categoria do mesmo.
 
<h1 align="center">
    <img src="/Gifs/Detalhesfilmes.gif">
</h1>

 <h3>
     Edição de Perfil/Senha
 </h3>
 
 O perfil pode ser alterado atualizando as informações do usuário no banco de dados SQLite3.
 
<h1 align="center">
    <img src="/Gifs/Editarperfil.gif">
</h1>
