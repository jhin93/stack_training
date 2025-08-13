# ========================
# Server Performance Stats
# ========================

# CPU total usage
cpu_total_usage=$(top -l 1 | grep "CPU" | head -n 1 | awk '{print $3+$5"%"}')
top5_cpu_procs=$(ps aux | sort -nrk 3 | head -n 6)

# Memory usage
mem_info=$(top -l 1 | grep PhysMem | head -n 1)
mem_used_raw=$(echo $mem_info | awk '{print $2}')
if [[ $mem_used_raw == *G ]]; then
  mem_used=$(echo $mem_used_raw | sed 's/G//')
  mem_used=$(awk "BEGIN {print $mem_used*1024}")
else
  mem_used=$(echo $mem_used_raw | sed 's/M//')
fi

mem_free_raw=$(echo $mem_info | awk '{print $6}')
if [[ $mem_free_raw == *G ]]; then
  mem_free=$(echo $mem_free_raw | sed 's/G//')
  mem_free=$(awk "BEGIN {print $mem_free*1024}")
else
  mem_free=$(echo $mem_free_raw | sed 's/M//')
fi

mem_total=$(awk "BEGIN {print $mem_used + $mem_free}")
mem_used_percent=$(awk "BEGIN {printf \"%.2f\", ($mem_used/$mem_total)*100}")
mem_free_percent=$(awk "BEGIN {printf \"%.2f\", ($mem_free/$mem_total)*100}")
top5_mem_procs=$(ps aux | sort -nrk 4 | head -n 6)

# Disk usage
disk_info=$(df -h / | tail -n 1)
disk_used=$(echo $disk_info | awk '{print $5}')
used_percent=$(echo $disk_used | sed 's/%//')
disk_free=$((100 - used_percent))

# Output
echo "===================="
echo "Server Performance Summary"
echo "===================="
echo ""
echo "CPU Usage: $cpu_total_usage"
echo "--------------------"
echo "Memory Used: ${mem_used_percent}%"
echo "Memory Free: ${mem_free_percent}%"
echo "--------------------"
echo "Disk Used: ${disk_used}%"
echo "Disk Free: ${disk_free}%"
echo ""
echo "--------------------"
echo "Top 5 Processes by CPU Usage"
echo "--------------------"
echo "$top5_cpu_procs"
echo ""
echo "--------------------"
echo "Top 5 Processes by Memory Usage"
echo "--------------------"
echo "$top5_mem_procs"