#!/bin/bash

# Coleta dados cpu
model=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | head -n1`
cores=`cat /proc/cpuinfo | grep -i 'cpu cores' | awk '{print $4}' | head -n 1`
threads=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | wc -l`
cpu_gen=`echo "${model}" | head -n1 | awk '{print $2}' | cut -c 4-4`

# Coleta dados memória
available_mem=`bc <<<"$(cat /proc/meminfo | grep -i memavailable | awk '{print $2}')/1024"`
total_mem=`bc <<<"$(cat /proc/meminfo | grep -i memtotal | awk '{print $2}')/1024"`
swap_total=`bc <<<"$(cat /proc/meminfo | grep -i swaptotal | awk '{print $2}')/1024"`
swap_free=`bc <<<"$(cat /proc/meminfo | grep -i swapfree | awk '{print $2}')/1024"`

# Escreve dados cpu
printf "
CPU

Modelo da CPU      ------------------ $model
Geração            ------------------ $cpu_genª geração
Qntd de núcleos    ------------------ $cores
Qntd de threads    ------------------ $threads



MEMÓRIA

Memória disponível ------------------ $available_mem M
Memória total      ------------------ $total_mem M
Swap total         ------------------ $swap_total M
Swap free          ------------------ $swap_free M
"