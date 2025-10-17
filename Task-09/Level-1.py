"""Changes done :
1) condition for Awarding the scolarship is gpa >= 3.5 and extracurricular_score >= 70
2) creating the empty array to avoid errors for the empty inputs 
3)  Raising ValueError for safe divide function when b is 0
4) using max function to find top student in top_student"""


import math

def calculate_gpa(grades):
    """Calculates GPA from a list of grades (0–100).Returns GPA on a 4.0 scale."""
    if not grades:
        return 0  

    avg = sum(grades) / len(grades)

    if avg > 90:
        return 4.0
    elif avg > 80:
        return 3.5
    elif avg > 70:
        return 3.0
    elif avg > 60:
        return 2.5
    elif avg > 50:
        return 2.0
    else:
        return 1.0 


def assign_scholarship(gpa, extracurricular_score):
    """
    Awards scholarship if:
    - GPA >= 3.5
    - Extracurricular score >= 70
    """
    if (gpa >= 3.5) and (extracurricular_score >= 70):
        return True
    else:
        return False


def normalize_scores(scores):
    """Normalizes scores to 0–1 range."""
    if not scores:
        return []
    max_score = max(scores)  
    return [s / max_score for s in scores]


def find_top_student(students):
    """Given a list of tuples (name, score), return the name of the top scorer."""
    top_student = max(students ,key=lambda x: x[1]) 
    return top_student[0]  


def safe_divide(a, b):
    """Divides a by b and rounds up."""
    if b == 0:
        raise ValueError("Value of b should be greater than 0")
    return math.ceil(a / b) 

