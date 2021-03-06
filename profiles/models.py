from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

import uuid


class UserProfile(models.Model):
    """
    A user profile for maintaining default
    delivery information and order history
    """
    # each user can only have one profile. And each profile can only
    # be attached to one user.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # delivery information fields we want the user to be able to
    # provide defaults for
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


# A quick receiver for the post save event from the user model.
# So that each time a user object is saved,  automatically
# either create a profile for them if the user has just been created.
# Or just save the profile to update it if the user already existed.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or Update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing Users: just save the profile
    instance.userprofile.save()


class SubscriberList(models.Model):
    subscriber_id = models.CharField(max_length=32,
                                     null=False,
                                     editable=False)
    email = models.EmailField(max_length=70, null=True,
                              blank=True, unique=True)

    # private method available only to ProductInventory Class
    def _generate_subscriber_id(self):
        """
        Generate a random, unique subscriber ID number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the subscriber ID
        if it hasn't been set already.
        """
        if not self.subscriber_id:
            self.subscriber_id = self._generate_subscriber_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subscriber_id
