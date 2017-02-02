#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    # You need to write this method
    """one_count = 0
    five_count = 0
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    six_count = 0
    value = 0
    if dice == []:
        return 0
    elif len(dice) == 1 and (dice[0] == 1):
        return 100
    elif len(dice) == 1 and (dice[0] == 5):
        return 50

    for num in dice:
        if num == 1:
            one_count = one_count + 1
            if one_count == 3:
                one_count = 10
            elif one_count == 4:
                one_count = 11
        elif num == 5:
            five_count = five_count + 1
            if five_count == 3:
                five_count = 10
        elif num == 2:
            two_count = two_count + 1
            if two_count == 3:
                value = 200
            else:
                value = 0
        elif num == 3:
            three_count = three_count + 1
            if three_count == 3:
                value = 300
            else:
                value = 0
        elif num == 4:
            four_count = four_count + 1
            if four_count == 3:
                value = 400
            else:
                value = 0
        elif num == 6:
            six_count = six_count + 1
            if six_count == 3:
                value = 600
            else:
                value = 0

    return one_count * 100 + five_count * 50 + value
    #for num in dice:
    #    if num = 1



    #pass"""
    if dice == []:
        return 0

    one = 100
    five = 50
    two = 0
    three = 0
    four = 0
    six = 0

    mydict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for num in dice:
        if num == 1:
            mydict[1] = mydict[1] + 1
        if num == 2:
            mydict[2] = mydict[2] + 1
        if num == 3:
            mydict[3] = mydict[3] + 1
        if num == 4:
            mydict[4] = mydict[4] + 1
        if num == 5:
            mydict[5] = mydict[5] + 1
        if num == 6:
            mydict[6] = mydict[6] + 1

    count_of_one = mydict[1] - 3
    if count_of_one >= 0:
        one = 1000 + (count_of_one * 100)
    else:
        one = mydict[1] * 100

    if mydict[2] >= 3:
        two = 200

    if mydict[3] >= 3:
        three = 300

    if mydict[4] >= 3:
        four = 400

    count_of_five = mydict[5] - 3
    if count_of_five >= 0:
        five = 500 + (count_of_five * 50)
    else:
        five = mydict[5] * 50

    if mydict[6] >= 3:
        six = 600
    return (one + two + three + four + five + six)


class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
