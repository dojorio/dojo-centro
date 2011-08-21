<?php
class Investigacao{

  private $suspeito;
  private $local;
  private $arma;
  
  function setTeoria($suspeito,$local,$arma){
    $this->suspeito = $suspeito;
    $this->local = $local;
    $this->arma = $arma;
  }

  function respostaTestemunha($suspeito, $local, $arma) {
    $opcoes = array();

    if($this->suspeito != $suspeito)
       $opcoes[] = 1;

    if($this->local != $local)
      $opcoes[] = 2;

     if($this->arma != $arma)
       $opcoes[] = 3;

    if (count($opcoes)== 0)
      return 0;
   
    $randomico = rand(0,count($opcoes)-1);

   return $opcoes[$randomico];
  }

}
