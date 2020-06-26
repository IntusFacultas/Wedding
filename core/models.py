from django.db import models

# Create your models here.


class ReservationControl(models.Model):
    email = models.CharField("Email", max_length=1024)
    extras = models.IntegerField("Extra People")


class Invitation(models.Model):
    email = models.CharField("Email", max_length=1024)


class RSVPPerson(models.Model):
    STATES_CHOICES = (
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AS", "American Samoa"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("DC", "District of Columbia"),
        ("FM", "Federated States of Micronesia"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("GU", "Guam"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MH", "Marshall Islands"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("MP", "Northern Mariana Islands"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PW", "Palau"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VI", "Virgin Islands"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming")
    )
    street = models.CharField("Street", max_length=1024)
    street2 = models.CharField("Street Line 2", max_length=1024)
    city = models.CharField("City", max_length=64)
    state = models.CharField("State", choices=STATES_CHOICES, max_length=2)
    dietary_restrictions = models.TextField("Dietary Restrictions")
    music_requests = models.TextField("Music Requests")
    name = models.CharField("Full Name", max_length=1024)
    invitation = models.ForeignKey(
        Invitation, related_name="people", on_delete=models.CASCADE)
