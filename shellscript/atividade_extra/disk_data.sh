#!/bin/bash

# Coleta dados
device_name=`df -H | grep -i sda2 | awk '{print $1}' | cut -c 6-9`
disk_total=`df -H | grep -i sda2 | awk '{print $2}'`
disk_used=`df -H | grep -i sda2 | awk '{print $3}'`

# Escreve dados
printf "${BOLD}
${WHITE}ARMAZENAMENTO

${GREEN}Dispositivo        ${WHITE}------------------------- ${device_name}
${GREEN}Capacidade total   ${WHITE}------------------------- ${disk_total/G/ Gb}
${GREEN}Capacidade usada   ${WHITE}------------------------- ${disk_used/G/ Gb}
\n\n"