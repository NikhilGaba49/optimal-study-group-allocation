# Importing the implementation of task 2 into task 3
from Project2_Valid_Study_Groups import valid_study_group

from itertools import combinations

# Define magic constants at the beginning of the program

MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 4

# Magic numbers used for scoring as per scoring instructions
SCORE_COMMON_SUBJECT = 3
SCORE_GROUP_OF_3 = 1
SCORE_GROUP_OF_4 = 2

def possible_study_groups(zbinis):
    """ This function takes a list of zoomerbinis (same as task 2), computes
    all the possible study groups that can be formed and returns these as a
    list of study groups (tuples) in descending score order as instructed.
    """
    
    # Firstly, we can find all study groups (of 3 and 4 members) based on the
    # index from the list of zoomerbinis
    # Note: these study group indices will be in ascending order 
    combinations_length_4 = [combination for combination in 
                             combinations(range(len(zbinis)), MAX_GROUP_SIZE)]
    combinations_length_3 = [combination for combination in 
                             combinations(range(len(zbinis)), MIN_GROUP_SIZE)]
    possible_combinations = combinations_length_4 + combinations_length_3
    
    # We test each study group validity from task 2 and keep valid study groups
    study_groups = [combination for combination in possible_combinations 
                        if valid_study_group(zbinis, combination)[0] is True]
    
    # We add scoring for each valid study group. 3 points are added for each
    # subject shared, plus 2 points if group of 4 or 1 point if group of 3
    study_groups_scores = []
    for study_group in study_groups:
        score = SCORE_COMMON_SUBJECT * valid_study_group(zbinis, 
                                                         study_group)[1]
        if len(study_group) == MAX_GROUP_SIZE:
            score += SCORE_GROUP_OF_4
        elif len(study_group) == MIN_GROUP_SIZE:
            score += SCORE_GROUP_OF_3
        study_groups_scores.append((study_group, score))
    
    # Finally, we arrange the study groups in descending score order
    study_groups_scores = sorted(study_groups_scores, 
                                 key=lambda study_group: study_group[1],
                                 reverse=True)
    return study_groups_scores