source venv/bin/activate
rm -rf build/ dist/ *.egg-info/
python3 -m build
twine upload dist/*
