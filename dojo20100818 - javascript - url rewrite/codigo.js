function rewrite(url){

    var pedacos_url = url.split('/')
    if(pedacos_url[1] == 'guide')
        return '/guide/'+pedacos_url[2]+'/2009/'+pedacos_url[4]
    if(pedacos_url[1] == 'company')
        return '/c'

    return '/article?id=' + pedacos_url[2]

}

