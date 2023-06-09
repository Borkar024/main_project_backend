from django.db import models



class Enquiry(models.Model):
    
    ENQUIRY_STATUS = [('Approved','Approved'),('Pending','Pending')]
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    mobile = models.CharField(max_length=13)
    message = models.TextField()
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=50, default='Pending', choices=ENQUIRY_STATUS)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)
