# !/bin/bash

# Coleta dados, todos são dados de socketes
todos=`bc <<<"$(ss -a | wc -l) - 1"`
em_espera=`bc <<<"$(ss -l | wc -l) - 1"`
conectados=`bc <<<"$(ss | wc -l) - 1"`
todos_tcp=`bc <<<"$(ss -at | wc -l) - 1"`
em_espera_tcp=`bc <<<"$(ss -lt | wc -l) - 1"`
conectados_tcp=`bc <<<"$(ss -t | wc -l) - 1"`

# Escreve dados
printf "ESTATÍSTICAS.DE.REDE Todos.os.sockets $todos Sockets.em.espera $em_espera Sockets.conectados $conectados Sockets.TCP $todos_tcp TCP.em.espera $em_espera_tcp TCP.conectados $conectados_tcp
\n\n"