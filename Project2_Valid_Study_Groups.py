# Importing the implementation of task 1 into task 2
from Project2_Attributes_Zbinis import zbini_attrs

# Define magic constants at the beginning of the program

MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 4

HAIRSTYLE = 0
COLOUR = 1
ACCESSORY = 2
SOCIAL_MEDIA = 3

# Magic numbers for each zoomerbini in a given study group
ZBINI_1 = 0
ZBINI_2 = 1
ZBINI_3 = 2
ZBINI_4 = 3

# A magic number representing the number of unique attributes if all 
# attributes are the same
ALL_SAME = 1

def valid_study_group(zbinis, group):
    """ This function takes a list of zoomerbinis (with type ids and the
    subjects each zoomerbini is taking) and potential study group as input. It
    determines if the study group is valid and returns this as a boolean value
    and the number of common subjects shared in the study group (if valid).
    """
    
    # Firstly, we check that the study group has only 3 or 4 members
    if len(group) not in (MIN_GROUP_SIZE, MAX_GROUP_SIZE):
        return (False, None)
    
    # We must check that no index is repeated in the group proposed
    if len(set(group)) != len(group):
        return (False, None)
    
    # We can filter the list of zoomerbinis for the concerned zoomerbinis only
    try:
        zbinis_filtered = [zbinis[index] for index in group]
    except IndexError:
        return (False, None)
    
    # Next, we determine whether there are any common subjects between the 
    # zoomerbinis in the study group and determine how many common subjects
    zbini_subjects = [set(subjects) for type_id, subjects in zbinis_filtered]
    common_subjects = zbini_subjects[ZBINI_1] & zbini_subjects[ZBINI_2] &\
        zbini_subjects[ZBINI_3]
    if len(group) == MAX_GROUP_SIZE:
        common_subjects = common_subjects & zbini_subjects[ZBINI_4]
    number_common_subjects = len(common_subjects)
    
    # The group is invalid if there are no subjects shared by the zoomerbinis
    if number_common_subjects == 0:
        return (False, None)
    
    # From task 1, we determine the attributes of each zoomerbini in the study
    # group and arrange these by attribute (for example, all hair/hat styles 
    # will be together
    attributes = [zbini_attrs(type_id) for type_id, subjects
                      in zbinis_filtered]
    hairstyles = {attribute[HAIRSTYLE] for attribute in attributes}
    colour = {attribute[COLOUR] for attribute in attributes}
    accessory = {attribute[ACCESSORY] for attribute in attributes}
    social_media = {attribute[SOCIAL_MEDIA] for attribute in attributes}
    
    # Now, we can check whether the attributes are all unique or all the same
    # and output the group validity and the number of common subjects shared
    attribute_same_unique = (ALL_SAME, len(group))
    if len(hairstyles) in attribute_same_unique and len(colour) in\
        attribute_same_unique and len(accessory) in attribute_same_unique and\
        len(social_media) in attribute_same_unique:
        return (True, number_common_subjects)
    else:
        return (False, None) 