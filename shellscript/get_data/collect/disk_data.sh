#!/bin/bash

# Coleta dados
device_name=`df -H | grep -i sda6 | awk '{print $1}' | cut -c 6-9`
disk_total=`df -H | grep -i sda6 | awk '{print $2}'`
disk_used=`df -H | grep -i sda6 | awk '{print $3}'`
disk_free=`df -H | grep -i sda6 | awk '{print $4}'`

# Envia dados
printf "ARMAZENAMENTO Dispositivo ${device_name} Capacidade.total ${disk_total/G/.Gb} Espaco.usada         ${disk_used/G/.Gb} Espaco.livre ${disk_free/G/.Gb}"