#! /bin/bash

url_validator(){
  echo "$1" | grep 'tp://w' > /dev/null
  o_padrao_eh_valido=$?
  if  [ $o_padrao_eh_valido -eq 0 ] ; then
    echo valido
  else
    echo invalido
  fi
}

test_deve_retornar_invalido_se_nao_houver_protocolo(){
  assertEquals 'invalido' $(url_validator '://whois.com')
}

test_deve_retornar_valido_quando_houver_protocolo_ftp_e_o_host(){
  assertEquals 'valido' $(url_validator 'ftp://whois.com')
}

test_deve_retornar_valido_quando_houver_protocolo_http_e_o_host(){
  assertEquals 'valido' $(url_validator 'http://whois.com')
}

test_deve_retornar_invalido_quando_nao_houver_host(){
  assertEquals 'invalido' $(url_validator 'ftp://')
}

# load shunit2
. ~/bin/shunit2

