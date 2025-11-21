from django.core.exceptions import ValidationError

import re

def validate_subject_name(subject_name):
    err_msg = "Subject must be in title case format."
    pattern = r'^[A-Z][a-z]+'
    for word in subject_name.split(" "):
        good_word = re.match(pattern,word)
        if not good_word:
            raise ValidationError(err_msg, params = {"subject_name" : subject_name})
    return subject_name


def validate_professor_name(professor):
    err_msg = 'Professor name must be in the format "Professor Adam".'
    pattern = r'^Professor [A-Z][a-z]+$'
    good_professor_name = re.match(pattern, professor)
    if good_professor_name:
        return professor
    else:
        raise ValidationError(err_msg, params = {"professor" : professor})