# Streamberry

**Streamberry** é uma plataforma de streaming fictícia desenvolvida com Django, inspirada em serviços como Netflix. A aplicação permite a gestão de filmes e séries, organização por gêneros, sistema de favoritos e controle de acesso baseado em permissões usando o decorador permission_required.

##  Funcionalidades Principais

* Cadastro e login de usuários com autenticação tradicional via **email** e senha.
* Sistema de permissões com papéis distintos:

  * **Assinante**: acesso ao catálogo e à sua lista de favoritos.
  * **Administrador**:

    * **Moderador**: gerenciamento de títulos e gêneros
    * **Gerente**: gerenciamento de assinantes e administradores
       * **Administrador padrão**: credenciais predefinidas para acesso total
* CRUD completo de:

  * Filmes
  * Séries
  * Temporadas
  * Episódios
  * Gêneros
  * Usuários (assinantes e administradores)

* Atribuição de múltiplos gêneros por título
* Sistema de favoritos ("Minha Lista")
* Upload de capas personalizadas para os títulos
* Player de vídeo com suporte a HLS (streaming adaptativo)

##  Autenticação e Redefinição de Senha

O sistema utiliza o modelo de usuário padrão do Django, com login via **emaiil** e senha. A redefinição de senha pode ser feita via e-mail (funcionalidade implementada).

As permissões são controladas por grupos e pelo campo `cargo` nos administradores:

* **Moderador**: CRUD de títulos e gêneros
* **Gerente**: gestão de assinantes e administradores

##  Estrutura do Projeto

* `usuario/`: autenticação, modelos de usuário, views e permissões
* `titulo/`: filmes e séries
* `temporada/`: temporadas e episódios
* `genero/`: classificação por gênero
* `favorito/`: controle da lista "Minha Lista"

## Configuração do arquivo `.env`
Para rodar a aplicação corretamente, crie um arquivo `.env` na raiz do projeto contendo as seguintes variáveis de ambiente:

```env
# Configurações do e-mail para envio (ex: redefinição de senha)
EMAIL_HOST_USER='seu-email@exemplo.com'        # Seu usuário de e-mail (ex: conta Gmail)
EMAIL_HOST_PASSWORD='sua-senha-de-email'       # Senha ou token de app do e-mail

# Domínio base da aplicação
DOMAIN_APP='http://localhost:8000'              # URL base onde a aplicação estará rodando
```

##  Como Executar Localmente

```bash
# Clone este repositório
git clone https://github.com/add-gutto/Streamberry.git
cd streamberry

# Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Atualize o pip e instale as dependências
pip install --upgrade pip
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie o superusuário
python manage.py createsuperuser

# Rode o servidor
python3 manage.py runserver
```

>  **Admin padrão:** `admin@gerente.com`
>  **Senha:** `admin123`

---


