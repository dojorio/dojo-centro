def traduz(comando)
    valor = comando.sub("mostra(", "print ")
    valor.sub!(")", "")
    valor.sub!("se Verdadeiro:", "if True:")

    return comando if valor == comando
    return valor
end 
