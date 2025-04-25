mkdir secured_logs
cp $(find vought_logs -name "*.txt") secured_logs
find vought_logs -type f -exec wc -c {} \; | sort -nr | head -n 1 | awk '{print $2}' > biggest_secret.txt
