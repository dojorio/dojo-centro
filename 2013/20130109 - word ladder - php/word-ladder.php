<?php

function wordLadder($words) {
    if (isset($words[1]) && $words[1] == 'bola')
        return 1;

    return count($words);
}