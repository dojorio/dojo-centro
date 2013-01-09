<?php

function proxima($palavra1, $palavra2) {
    return levenshtein($palavra1, $palavra2) === 1;
}

function andar_dfs($word, $words, &$javi = array()) {
    $total = 1;
    $javi[$word] = 1;

    foreach($words as $otherWord) {
        if (!isset($javi[$otherWord]) && proxima($word, $otherWord)) {
            $total += andar_dfs($otherWord, $words, $javi);
        }
    }

    return $total;
}

function wordLadder($words) {
    $total = 0;
    $javi = array();

    foreach ($words as $word) {
        $total = max($total, andar_dfs($word, $words, $javi));
    }

    return $total;
}