echo " BUILD START"
python3.9  -m pip install -r requirements.txt
python3.9 manage.py build --output public
echo " BUILD END"