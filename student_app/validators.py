from django.core.exceptions import ValidationError

import re

def validate_locker_combination(locker_combination):
    err_msg = 'Combination must be in the format "12-12-12"'
    pattern = r'^\d{2}-\d{2}-\d{2}$'
    good_locker_combination = re.match(pattern,locker_combination)
    if good_locker_combination:
        return locker_combination
    else:
        raise ValidationError(err_msg, params = {'locker_combination' : locker_combination})

def validate_email(student_email):
    pattern = r'[A-Za-z0-9]+@school\.com'
    err_msg = 'Invalid school email format. Please use an email ending with "@school.com".'
    good_email = re.match(pattern, student_email)
    if good_email:
        return good_email
    else:
        raise ValidationError(err_msg, params = {"student_email" : student_email})

def validate_name(name):
    pattern = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'
    err_msg = 'Name must be in the format "First Middle Initial. Last"'
    good_name = re.match(pattern, name)
    if good_name:
        return name
    else:
        raise ValidationError(err_msg, params = {"name" : name})