follow these command to run this project

git clone https://github.com/Vijayvarma115/bluestock-ipo-webapp.git
cd bluestock-ipo-webapp
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
