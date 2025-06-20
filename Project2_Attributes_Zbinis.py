# Define magic constants at the beginning of the program

MAX_NUMBER_ZBINIS = 256

HAIRSTYLE_COLLECTIONS = 64
COLOUR_COLLECTIONS = 16
ACCESSORY_COLLECTIONS = 4

# A magic number representing the alternate characteristics in sets of 4
ALTERNATING = 4

def zbini_attrs(type_id):
    """This function zbini_attrs accepts the type_id of the Zoomberini,
    determines its unique attributes and returns these as a tuple of strings.
    """
    # zoomberinis only have integer type ids from 0 to 255(inclusive)  
    if type_id not in range(MAX_NUMBER_ZBINIS):
        return None
    
    # zoomberinis' hair/hat styles are arranged in collections of 64 elements
    hair_hat_dict = {0: "wavy", 1: "curly", 2: "beanie", 3: "cap"}
    hair_hat = hair_hat_dict.get(type_id // HAIRSTYLE_COLLECTIONS)
    
    # zoomberinis' favourite colours are arranged in collections of 16 elements
    # alternating through each of the 4 colours in order
    colour_dict = {0: "red", 1: "blue", 2: "yellow", 3: "green"}
    colour = colour_dict.get(type_id // COLOUR_COLLECTIONS % ALTERNATING)
    
    # zoomberinis' fashion accessories are arranged in collections of 4 
    # elements, alternating through each of the 4 accessories in order
    accessory_dict = {0: "sneakers", 1: "bowtie", 2: "sunglasses", 3: "scarf"}
    accessory = accessory_dict.get(type_id // ACCESSORY_COLLECTIONS % 
                                   ALTERNATING)
    
    # zoomberini's preferred social media alternates between 4 platforms
    social_dict = {0: "tiktok", 1: "instagram", 2: "discord", 3: "snapchat"}
    social = social_dict.get(type_id % ALTERNATING)
    
    return hair_hat, colour, accessory, social