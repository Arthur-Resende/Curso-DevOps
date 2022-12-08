#!/bin/bash

if [ $OPTIND == 1 ]; then
    email=arthur.faria@globalhitss.com.br
    limit=90
fi

while getopts e:l:h flag
do
    case "${flag}" in
        e) email="${OPTARG}";;
        l) limit="${OPTARG}";;
        h) cat ./help && exit 0;;
    esac
done

while true; do
    cpu_use_raw=`sar 1 1 | head -n4 | tail -n1 | tr , . | awk '{print $8}'`
    cpu_use=`bc <<<"100 - ${cpu_use_raw}"`

    if [ "${cpu_use%%.*}" -ge $limit ]; then
        echo "Uso do cpu está em ${cpu_use}%, sendo igual ou maior que a marca de ${limit}%, alerta será enviado por email para ${email}."
        echo "Alerta, o uso de cpu da máquina superou ${limit}%" | mail -s "Alerta" "${email}"
        echo "Email enviado"
        sleep 60
    fi
done