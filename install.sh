rm ./dist/enckey-0.0.1.tar.gz
rm -r ./enckey.egg-info
pip install -r requirements.txt
python setup.py clean
python setup.py sdist
pip uninstall enckey
pip install ./dist/enckey-0.0.1.tar.gz
