<?php


function andar($word, $words, $javi=array()) {
    $total = 1;
    $javi[$word] = 1;

    foreach($words as $otherWord) {
        if (!$javi[$otherWord] && (levenshtein($word, $otherWord) == 1)) {
            $total += andar($otherWord, $words, $javi);
        }
    }
    return $total;
}

function wordLadder($words) {
    $total = 1;
    $caminhos = array();
    foreach ($words as $word) {
        $caminhos[$word] = andar($word, $words);
    }

    if (count($words) >= 2 && levenshtein($words[0], $words[1]) == 1)
        $total++;

    if (count($words) >= 3 && levenshtein($words[1], $words[2]) == 1)
        $total++;

    else if (count($words) >= 3 && levenshtein($words[0], $words[2]) == 1)
        $total++;
    
    if (count($words) >= 4 && levenshtein($words[0], $words[3]) == 1)
        $total++;
    
    else if (count($words) >= 4 && levenshtein($words[2], $words[3]) == 1)
        $total++;

    return $total;
}