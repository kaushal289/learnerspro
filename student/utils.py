from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .models import Student

import six



class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp) :

        customer = Student.objects.get(user=user.pk)

        return six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(customer.email)

generate_token = TokenGenerator()