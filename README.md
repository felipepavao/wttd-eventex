# Eventex 

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/felipepavao/wttd-eventex.svg?branch=master)](https://travis-ci.org/felipepavao/wttd-eventex)
[![Code Climate](https://codeclimate.com/repos/5691a8da557dd85c4a001894/badges/52b046b2c35cf7662211/gpa.svg)](https://codeclimate.com/repos/5691a8da557dd85c4a001894/feed)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@gihub.com:felipepavao/wttd-eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para o Heroku

```console
heroku create minha-instancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o e-mail
git push heroku master --force
```
