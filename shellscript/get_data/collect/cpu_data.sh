#!/bin/bash

# Coleta dados
model=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $4" "$5" "$6" "$7" "$8" "$9}' | head -n1 | tr ' ' '.'`
cores=`cat /proc/cpuinfo | grep -i 'cpu cores' | awk '{print $4}' | head -n 1`
threads=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | wc -l`
cpu_gen=`echo "$(echo $model | tr '.' ' ')" | head -n1 | awk '{print $3}' | cut -c 4-4`

echo "$(echo Intel(R).Core(TM).i3-2310M.CPU.@.2.10GHz | tr ' ' '.')" | head -n1 | awk '{print $3}' | cut -c 4-4

# Escreve dados
printf "CPU Modelo.da.CPU $model Geracao $cpu_genª.geracao Qntd.de.threads $threads Qntd.de.nucleos $cores"