#! /bin/bash
set -ex;

pip install -r /workspaces/coffee_shop_employee_service/requirements.txt

# Enable project to use .env
echo "export USE_DOT_ENV=True" >> $HOME/.bashrc && source $HOME/.bashrc
