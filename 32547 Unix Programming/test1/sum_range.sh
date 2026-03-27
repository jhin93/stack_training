# !/user/bin/bash env

START=$1
END=$2

SUM=0

NUM=$START

while [ $NUM -le $END ]
do
  SUM=$((SUM + NUM))
  NUM=$((NUM + 1))
done

echo $SUM

