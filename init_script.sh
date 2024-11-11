#!/bin/bash

# Diretório do ambiente virtual
VENV_DIR=".venv"

# Criar o ambiente virtual se ele não existir
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi

# Ativar o ambiente virtual
source $VENV_DIR/bin/activate

# Instalar as dependências
pip install -r ./requirements.txt
