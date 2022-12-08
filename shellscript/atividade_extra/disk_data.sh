#!/bin/bash

# Coleta dados
device_name=`df -H | grep -i sda6 | awk '{print $1}' | cut -c 6-9`
disk_total=`df -H | grep -i sda6 | awk '{print $2}'`
disk_used=`df -H | grep -i sda6 | awk '{print $3}'`
disk_free=`df -H | grep -i sda6 | awk '{print $4}'`

# Escreve dados
printf "${BOLD}
${WHITE}ARMAZENAMENTO

${GREEN}Dispositivo        ${WHITE}------------------------- ${device_name}
${GREEN}Capacidade total   ${WHITE}------------------------- ${disk_total/G/ Gb}
${GREEN}Espaço usada       ${WHITE}------------------------- ${disk_used/G/ Gb}
${GREEN}Espaço liver       ${WHITE}------------------------- ${disk_free/G/ Gb}
\n\n"