# !/bin/bash

# Coleta dados, todos são dados de socketes
todos=`bc <<<"$(ss -a | wc -l) - 1"`
em_espera=`bc <<<"$(ss -l | wc -l) - 1"`
conectados=`bc <<<"$(ss | wc -l) - 1"`
todos_tcp=`bc <<<"$(ss -at | wc -l) - 1"`
em_espera_tcp=`bc <<<"$(ss -lt | wc -l) - 1"`
conectados_tcp=`bc <<<"$(ss -t | wc -l) - 1"`

# Escreve dados
printf "${BOLD}
${WHITE}Estatísticas de socketes

${GREEN}Todos os sockets   ${WHITE}------------------------- $todos
${GREEN}Sockets em espera  ${WHITE}------------------------- $em_espera
${GREEN}Sockets conectados ${WHITE}------------------------- $conectados
${GREEN}Sockets TCP        ${WHITE}------------------------- $todos_tcp
${GREEN}TCP em espera      ${WHITE}------------------------- $em_espera_tcp
${GREEN}TCP conectados     ${WHITE}------------------------- $conectados_tcp
\n\n"