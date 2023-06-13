#./seed_database.sh
#chmod u+x ./startup.sh


rm db.sqlite3
rm -rf ./teatimeapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations teatimeapi
python3 manage.py migrate teatimeapi
python3 manage.py loaddata tea_type
python3 manage.py loaddata teas

