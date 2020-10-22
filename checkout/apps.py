from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Overriding the ready method and importing our signals module.
    # Every time a line item is saved or deleted, Our custom update
    # total model method will be called. Updating the order totals
    # automatically.
    def ready(self):
        import checkout.signals
