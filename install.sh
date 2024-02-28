#!/bin/bash

project_domain=""
project_path=$(pwd)
current_user=$USER

read -p "Имя домена без протокола (ex: yandex.ru): " project_domain

echo "Установка Python зависимостей"

poetry install --no-root
poetry shell
gunicorn_path=$(which python)

echo "Копирование конфига nginx в файл конфига домена"

IFS="." read -ra parts <<< "$project_domain"
domain_name=${parts[0]}
nginx_file_name="$domain_name.conf"
cp nginx/site.conf "nginx/$nginx_file_name"

echo "Смена вхождения строк на нужные значения"

sed -i "s~fa_template_path~$project_path~g" systemd/gunicorn.service "nginx/$nginx_file_name"
sed -i "s~fa_gunicorn_path~$gunicorn_path~g" systemd/gunicorn.service
sed -i "s~fa_user~$current_user~g" systemd/gunicorn.service
sed -i "s~fa_template_domain~$project_domain~g" "nginx/$nginx_file_name"

echo "Создание ссылок на файлы systemd и nginx"

sudo ln -s "$project_path/$nginx_file_name" /etc/nginx/sites-enabled/
sudo ln -s "$project_path/systemd/gunicorn.service" /etc/systemd/system/

echo "Запуск systemd-daemon и nginx"

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart