#!/bin/bash


if [ "$#" -lt 1 ]
then
echo "Usage parse_log.sh /path/to/your.log"
exit
fi

sed -n '/key=/p' $1 > aux.txt
grep 'key='   aux.txt | cut -d '_' -f2   > aux0.txt
grep '[0-9/]_event'  aux.txt | cut -d '_' -f4   > aux4.txt
grep '[0-9/]Collection'   aux.txt | cut -d 't' -f2   > aux5.txt
grep 'Prob: ' aux.txt | awk '{print $3}' > aux1.txt
grep 'Prob: ' aux.txt | awk '{print $6}' > aux2.txt
grep 'Prob: ' aux.txt | awk '{print $8}' > aux3.txt

echo 'Subrun Event Type Num0 Pred Prob'| column -t > test.csv 
paste aux4.txt aux5.txt aux0.txt aux1.txt aux2.txt aux3.txt | column -t >> test.csv 
rm  aux.txt aux0.txt aux1.txt aux2.txt aux3.txt aux4.txt aux5.txt

