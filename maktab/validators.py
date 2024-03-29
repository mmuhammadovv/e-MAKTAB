from django.core.exceptions import ValidationError


def file_size(value):
    filesize =value.size
    if filesize > 1024000000:
        raise ValidationError("maximum value is 512 mb")