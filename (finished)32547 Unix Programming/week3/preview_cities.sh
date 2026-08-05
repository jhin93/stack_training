N=${1:-10}   # If $1 not provided, default to 10

echo "First $N lines from cities.txt"
head -n "$N" cities.txt

echo
echo "Total lines:"
wc -l cities.txt
