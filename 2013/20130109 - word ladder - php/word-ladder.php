<?php

function wordLadder($words) {
    $escada = array($words[0]);
    $total = 1;

    sort($words);

    for ($i = 0; $i < count($words); $i++) {
        $palavra1 = $words[$i];

        foreach ($words as $palavra2) {
            if ($palavra1 == $palavra2)
                continue;

            if (levenshtein($palavra1, $palavra2) == 1)
                $total++;
        }

        
    }

    return $total;
}