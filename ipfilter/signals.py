from django.dispatch import Signal
excluded_ip_found = Signal(providing_args=["request", "ip"])
