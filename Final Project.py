# MATH4581 - Final Project
# Katie Geisler, Nia Quinn - April 2024

# H_0 is that the distrubution of the 20 most frequent words in the Bible observe Zipf's Law.

# Determining the accuracy of Zipf's Law with The Bible 
import scipy.stats as stats 
import numpy as np 

# Setting Constants
# total_word_count = 788258
total_word_count = 212777
df = 19

N = 21 # N = 20, but adjusted to account for non-inclusive for loop [1, 21)

denominator_prob = 0
# calculating the denominator constant for Zipf's Law
for i in range(1, N): # [1, 21)
    denominator_prob += 1 / (i + 2.7)

# Top 20 words accessed from https://www.kingjamesbibleonline.org/Popular-Bible-Words.php
# the index of the number indicates it's frequency in the bible
observed_top_20 = [28364, 28269, 21257, 12044, 11683, 
                   11285, 9022, 8684, 8362, 7582, 
                   7365, 7127, 6796, 6664, 6638, 
                   6579, 6568, 6442, 6073, 5973]

# probabilities of top 20 most frequent words
prob_top_20_words = [0 for i in range(20)]

# expected value of top 20 words
expected_top_20 = [0 for i in range(20)]

# We then calculate the probability of the top 20 most common words
for k in range(1, N):
    prob_top_20_words[k - 1] = 1 / (k + 2.7) / denominator_prob

# The next step is to calculate the expected value of each of the top 20 words
for i in range(1, N):
    expected_top_20[i - 1] = prob_top_20_words[i - 1] * total_word_count

chi_square_test_statistic, p_value = stats.chisquare( 
    f_obs=observed_top_20, f_exp=expected_top_20) 

if p_value < 0.05:
    print("Reject H_0. The observed distribution of words in the Bible doesn't follow Zipf's Law.")
else:
        print("Fail to reject H_0. The observed distribution of words in the Bible does follow Zipf's Law.")