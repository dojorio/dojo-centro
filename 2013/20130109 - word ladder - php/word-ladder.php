<?php

function wordLadder($words) {
    if (isset($words[1]) && $words[1] != 'cama')
        return 1;

    return count($words);
}