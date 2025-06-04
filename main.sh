set -e

python3 -m src.main 
cd docs && pwd &&  python3 -m http.server 8888