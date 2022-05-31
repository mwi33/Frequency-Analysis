# Frequency analysis

## Overview

One method of identifying encrpytion keys for simple substituion ciphers, is to conduct a 'Frequency Analysis' which is to simply count the occurance of each letter of the cipher.  Traditionally, within the english language, certain letters tend to occur more frequently.  My analysing the frequency of the letters in the ciphertext, a prediction to which letters have been substituted.  

The letters 'ETAO' are the most frequeny letters in the english language.  The image below shows the distrubution of each letter of the english language.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/English_letter_frequency_%28alphabetic%29.svg/1920px-English_letter_frequency_%28alphabetic%29.svg.png" width="500" height="500">

## Function

## Libraries

1.  [matplotlib](https://matplotlib.org/)

## Classes

1.  Frequency_analysis

## Methods

1.  load_data()
2.  count_upper_characters()
3.  count_lower_characters()
4.  sum_upper_lower_characters()
5.  calculate_percentages()
6.  plot_analysis()

### Arguments

1.  data_file - this is the utf-8 encoded text that is to be analysed.  It is provided as a txt file and passed as an argument when instanciating a Frequency_Analysis object.

### Class variables

1.  data - holds the text that will be analysed.  It is created when the object is created and is loaded with data when the 'load_cipher' method is run.

## Unit tests

## Implementation rationale

Decision 1 - Separation of counting upper and lower characters into separate methods.

Rationale - Design decision provides additional flexibility in being able to obtain the count of these separate measure individually.
