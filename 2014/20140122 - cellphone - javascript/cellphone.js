cellphone = function(words){
  
    var dictionary = new Array();

    for(i = 0; i < words.length; i++){
        dictionary[words[i][0]] |= 0;
        dictionary[words[i][0]]++;
    }


    console.dir(dictionary.length);

    if(words.length == dictionary.length){
        return 1;    
    }

    if(words.length == 1) {
        return 1
    }else{
        if(words[1].indexOf(words[0]) == 0 ||
        words[0].indexOf(words[1]) == 0
    ){
            return 1.5;
        }else if (words[0][0] == words[1][0]){
            return 2
        }else{
            return 1
        }
    }
}



module.exports = cellphone;
