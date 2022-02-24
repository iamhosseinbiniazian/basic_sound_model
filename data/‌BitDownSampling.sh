mkdir converted
for i in *.wav; do 
  sox -S "$i" -b 32 converted/"$i"; 
done
