from django.dispatch import Signal


user_linked_to_response = Signal(providing_args=["response"])
