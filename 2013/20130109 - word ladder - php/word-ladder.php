<?php

function wordLadder($words) {
    if (count($words) == 1) return 1;
    if (levenshtein($words[0], $words[1]) == 1)
        return 2;
    return 1;
}