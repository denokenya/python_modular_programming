# A program to grade students results

def grade(score):
    """
    A function to grade student results

    Parameters: score
        Type:int

    Return Value :letter
        Type:'Char'

    """ 
    score = int(input("What is the score"))
    if score >= 70:
        letter = 'A'
    elif score >= 60:
        letter = 'B'
    elif score >= 50:
        letter = 'C'
    elif score >= 40:
        letter = 'D'
    else:
        letter = 'F'
    return letter
