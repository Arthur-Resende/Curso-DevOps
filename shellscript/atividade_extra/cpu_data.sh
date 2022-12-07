#!/bin/bash

# Coleta dados
model=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $4" "$5" "$6" "$7" "$8" "$9}' | head -n1`
cores=`cat /proc/cpuinfo | grep -i 'cpu cores' | awk '{print $4}' | head -n 1`
threads=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | wc -l`
cpu_gen=`echo "${model}" | head -n1 | awk '{print $3}' | cut -c 4-4`

# Escreve dados
printf "${BOLD}
${WHITE}CPU

${GREEN}Modelo da CPU      ${WHITE}------------------------- $model
${GREEN}Geração            ${WHITE}------------------------- $cpu_genª geração
${GREEN}Qntd de threads    ${WHITE}------------------------- $threads
${GREEN}Qntd de núcleos    ${WHITE}------------------------- $cores
\n\n"