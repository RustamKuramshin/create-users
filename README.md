##### Заведение пользователей

Запуск (сначала нужно прописать креды в database.ini, подложить roles.json и users.json)
```shell
python3 Main.py
```

Перед запуском скрипта, нужно установить зависимости (возможно список не полный):
```shell
pip3 install psycopg2
pip3 install psycopg2-binary
sudo apt install postgresql-client-common
sudo apt-get install libpq-dev python-dev
sudo apt-get install build-dep python-psycopg2
sudo apt install python3-psycopg2
sudo apt install postgresql-client-12
```

Есть режим dry-run
```shell
python3 Main.py --dry-run
```