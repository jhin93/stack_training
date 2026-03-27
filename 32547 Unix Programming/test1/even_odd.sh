# !/user/bin/bash env

NUM=$1


if [ $(( NUM%2 )) -eq 0 ]
then
	echo "Even"
else
	echo "Odd"
fi

