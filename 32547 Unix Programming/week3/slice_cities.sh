echo -n "Head or Tail? (h/t)"
read MODE

echo -n "How many lines? "
read N

[ "$MODE" = "h" ] && head -n "$N" cities.txt
[ "$MODE" = "t" ] && tail -n "$N" cities.txt
