# Importing the implementation of task 3 in task 4
from Project2_Possible_Study_Groups import possible_study_groups

from itertools import combinations

# Define magic constants at the beginning of the program

MIN_GROUP_SIZE = 3

# Magic numbers used for tiebreaking to determine optimal allocation
IDX_NUM_ZOMB_ALLC = 1
IDX_COMB_SCORE = 2
IDX_MIN_IDX = 3
IDX_SCND_MIN = 4
IDX_THRD_MIN = 5

def combined_study_groups(allocation):
    """ This function accepts an allocation (tuple of tuples) as input and
    returns one single tuple, containing study groups indices. 
    """
    combined_study_group = ()
    # This is needed so that no index appears more than once in an allocation
    for study_group in allocation:
        combined_study_group += study_group
    return combined_study_group

def tiebreaking(possible_allocations, study_groups_scores, study_groups):
    """ 
    Inputs: All the possible allocations, study_groups and their scores
    Computation: Determines the number of zoomerbinis allocated, combined score
    of the allocation, the minimum index, the second minimum index and the 
    third minimum index needed for tiebreaking for each allocation
    Output: A list with all allocations and their associated properties.
    """
    
    allocations = []
    for allocation in possible_allocations:
        
        # We ask for single tuple of zoomerbinis allocated, as this will be
        # helpful for several tiebreaking rules
        combined_indices = sorted(combined_study_groups(allocation))
        number_zbinis_allocated = len(combined_indices)
        
        # We can determine combined score by adding scores of each study group
        score = 0
        for study_group in allocation:
            score += study_groups_scores[study_groups.index(study_group)][1]
        
        # We also compute the minimum, second minimum and the third minimum 
        # index for each allocation from the sorted single tuple 
        minimum_index = combined_indices[0]
        second_minimum_index = combined_indices[1]
        third_minimum_index = combined_indices[2]
        
        allocations.append((allocation, number_zbinis_allocated, score, 
                                minimum_index, second_minimum_index, 
                                third_minimum_index))
        
    return allocations
    
def alloc_study_groups(zbinis):
    """ This function accepts a list of zoomerbinis (similar to tasks 2 and 3)
    and computes the optimal allocation of study groups (that is, an allocation
    in which the maximum number of zoomerbinis can be allocated). The output
    is a list of tuples, with each tuple being a study group with indices into
    the input list of zoomerbinis.
    """
    
    # Find all possible study groups (task 3) with the list of zoomerbinis
    # and their corresponding scores
    study_groups_scores = [study_group for study_group in 
                               possible_study_groups(zbinis)]
    study_groups = [group for group, score in study_groups_scores]
        
    # Find all valid allocations from those study groups. Since study groups
    # must have at least 3 zoomerbinis, the allocations can be limited to the 
    # number of zoomerbinis divided by the minimum group size
    possible_allocations = []
    for i in range(len(zbinis) // MIN_GROUP_SIZE, 0, -1):
        for allocation in combinations(study_groups, i):
            combined_indices = combined_study_groups(allocation)
            if len(set(combined_indices)) == len(combined_indices):
                possible_allocations.append(allocation)
    
    # We determine the unique properties of each allocation to assist with
    # deciding which allocation is ultimately optimal
    allocations = tiebreaking(possible_allocations, study_groups_scores, 
                                  study_groups)
        
    try:
        # We can now arrange the allocations in a descending order based on the
        # number of zoomerbinis allocated (and subsequent tiebreaking)
        
        sorted_possible_allocations = sorted(
            allocations, 
            key=lambda alloc: (alloc[IDX_NUM_ZOMB_ALLC], alloc[IDX_COMB_SCORE], 
                               -alloc[IDX_MIN_IDX], -alloc[IDX_SCND_MIN], 
                               -alloc[IDX_THRD_MIN]),
            reverse=True)
        # The best allocation will be the first allocation in the sorted list
        optimal_allocation = list(sorted_possible_allocations[0][0])
    
    # If no study group is possible, there is no optimal allocation
    except IndexError:
        optimal_allocation = []
        
    return optimal_allocation      