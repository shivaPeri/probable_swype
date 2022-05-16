# Probable Swype

This repo is part of a larger project which entails creating an experimental digital keyboard swype interface in which, _instead of your fingers going to the keys, the keys come to your fingers._

One might wonder, how do we know which keys to should appear with larger probabilites? Using the [Wikipedia Word Frequencies](https://github.com/IlyaSemenov/wikipedia-word-frequency/blob/master/results/enwiki-20210820-words-frequency.txt) repo, this python script (work in progress) computes the necessary data structure for queries the apppropriate probabilities. Although I heavily took inspiration from the ideas of Viterbi decoding, this script should recursively compute the necessary letter proababilites given an input string using only word frequencies from public data.

<img width="1440" alt="kaliedescope_slide" src="https://user-images.githubusercontent.com/57304890/168505920-73efdc35-51d7-4ef2-8dbd-200cb6342557.png">
