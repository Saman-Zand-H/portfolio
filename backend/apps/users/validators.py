import os
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


def image_validator(file):
    name, ext = os.path.splitext(file.name)
    valid_exts = ["png", "jpeg", "jpg"]
    if ext not in valid_exts:
        raise ValidationError(_("invalid extenstion for image."))
