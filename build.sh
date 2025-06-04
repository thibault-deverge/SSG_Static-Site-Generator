set -e

if [ -z "$1" ]; then
  BASEPATH="/${SSG_Static-Site-Generator}/"
else
  BASEPATH="$1"
fi

python3 -m src.main "$BASEPATH"