total = 0  # >= 101 ; maximize:total 
total_set = [[('black', 6), ('black', 7), ('red', 8)],
             [('black', 1), ('black', 2), ('black', 3)]]  # if check function returns true, add here.

double_set = [[('yellow',5),('yellow',6)],
          [('black',12),('black',12)], 
          [('red',1),('red',2)], 
          [('blue',2),('blue',2)], 
          [('red',3),('red',3)], 
          [('black',10),('black',10)], 
          [('red',1), ('red',1)]]

def check_Set(Set: list) -> bool:
    """
    Check if a given list of tiles represents a valid "Set".

    Parameters:
    Set (list): A list of two-character strings representing tiles, where the first character is a letter
        representing the tile's color (e.g. "red"), and the second character is a number representing
        the tile's value (e.g. "5").

    Returns:
    bool: True if the given list of tiles represents a valid set, False otherwise.

    A valid set can be either a "run set" or a "group set":
    - Run Set: At least three tiles with consecutive numbers and the same color, up to a maximum of 13 tiles.
    - Group Set: At least three tiles with the same number but different colors, up to a maximum of four tiles.
    The function checks whether the given set meets these requirements, and returns True if it does, and False otherwise.
    """
    color, number = [], []
    MIN_SET_LENGTH = 3
    MIN_COLOR_LENGTH = 3
    MAX_COLOR_LENGTH = 4

    for idx, clr in enumerate(Set):
        color.append(Set[idx][0])
        number.append(Set[idx][1])

    min_val, max_val = min(number), max(number)
         
    if len(number) < MIN_SET_LENGTH:
        return False
    
    # Calculate Run Set
    if max_val - min_val + 1 == len(number):
        def check_run(Set):
            for tile in range(len(number)):
                diff = number[tile] - min_val
                if number[tile] > 0:
                    number[tile] = number[diff]
                else:
                    return False

            if len(set(color)) == 1:
                return True
            else:
                return False
        
        is_run_set = check_run(Set)
        return is_run_set
    
    # Calculate Group Set
    if len(set(number)) == 1:
        def check_group(Set: list) -> bool:
            color, number = [], []

            for idx, clr in enumerate(Set):
                color.append(Set[idx][0])
                number.append(Set[idx][1])

            if len(set(color)) == MIN_COLOR_LENGTH or len(set(color)) == MAX_COLOR_LENGTH:
                if len(number) == MIN_COLOR_LENGTH or len(number) == MAX_COLOR_LENGTH:
                    return True
                else: 
                    return False  
            else: 
                return False
                
        is_group_set = check_group(Set)
        return is_group_set
    else:
        return False
    

def check_double_set(Set:list) -> bool:
    """
    Checks if a given set contains at least 5 pairs of double elements.
    
    Parameters:
    - Set: a list of elements

    Returns:
    - True if the set contains at least 5 pairs of double elements (i.e., elements with length 2 and the same characters), False otherwise.

    Side effects:
    - Updates the global variable current_set_count with the number of pairs of double elements found in the set.
    """
    global current_set_count
    current_set_count = 0
    SET_LENGTH = 2
    MAX_SET_COUNT = 5
    
    
    for i in Set:
        if len(i) == SET_LENGTH and i[0] == i[1]:
            current_set_count += 1
        else:
            pass
    
    if current_set_count >= MAX_SET_COUNT:
        return True
    else:
        return False
    

def calculate_rack_normal(Set:list) -> str:
    """
    Calculates the total score of a given set of numbers and determines whether or not the score is high enough
    to proceed.

    Parameters:
        Set (list): A list of tuples representing cards in the set. Each tuple consists of a color and a number.

    Returns:
        str: A string indicating whether or not the score is high enough to proceed.
    """
    number = []
    MIN_SCORE = 101
    global total
    
    for set in Set:
        for idx, clr in enumerate(set):
            number.append(set[idx][1])
    total = sum(number)
    
    if total >= MIN_SCORE:
        print('Eliniz Açar.')
    else:
        print('Eliniz Açmaz.') 
        print(f'Açmak için kalan puan: {MIN_SCORE - total}')


def calculate_rack_double(Set:list) -> str:
    """
    Determines whether or not a given set of cards contains a valid "double set" according to the rules of the game.
   
    Parameters:
        Set (list): A list of tuples representing cards in the set. Each tuple consists of a color and a number.

    Returns:
        str: A string indicating whether or not the set contains a valid double set and how many valid sets are in it.
    """
    TOTAL_SET_COUNT = 5

    if check_double_set(Set):
        print(f'El açar. Toplam geçerli per sayısı: {current_set_count}')
    else:
        print(f'Eliniz Açmaz. Güncel geçerli per sayısı: {current_set_count}')
        print(f'El açmak için gerekli olan per sayısı: {TOTAL_SET_COUNT - current_set_count}')


def calculate(set_type:str) -> None:
    """
    Calculate score for a rack based on set type.

    Args:
        set_type (str): The set to be used: 'Normal Set' or 'Double Set'.

    Returns:
        None.
    """
    if set_type == 'Normal Set':
        calculate_rack_normal(Set=total_set)
    elif set_type == 'Double Set':
        calculate_rack_double(Set=double_set)
    else:
        print('Lütfen set türünüzü seçiniz.')