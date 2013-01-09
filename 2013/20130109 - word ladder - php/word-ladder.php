<?php

function wordLadder($words) {
    $total = 1;

    if (count($words) >= 2 && levenshtein($words[0], $words[1]) == 1)
        $total++;

    if (count($words) >= 3 && levenshtein($words[1], $words[2]) == 1)
        $total++;

    else if (count($words) >= 3 && levenshtein($words[0], $words[2]) == 1)
        $total++;

    return $total;
}