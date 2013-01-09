<?php

function proxima($palavra1, $palavra2) {
    return levenshtein($palavra1, $palavra2) === 1;
}

function andar_dfs($word, $words, &$javi = array()) {
    $total = 0;
    $javi[$word] = 1;

    foreach($words as $otherWord) {
        if (!isset($javi[$otherWord]) && proxima($word, $otherWord)) {
            $total = max($total, andar_dfs($otherWord, $words, $javi));
        }
    }

    return $total +1;
}

function wordLadder($words) {
    $total = 0;

    foreach ($words as $word) {
        $total = max($total, andar_dfs($word, $words));
    }

    return $total;
}