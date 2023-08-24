from django.db.models import TextChoices
from django.utils.translation import gettext as _


class Genders(TextChoices):
    male = "M", _("male")
    female = "F", _("female")
    just_stupid = "U", _("unknown")
