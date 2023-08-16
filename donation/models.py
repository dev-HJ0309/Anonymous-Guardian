from django.db import models

from AnonymousGuardian.models import Period, Validity
from member.models import Member


# Create your models here.
class DonationHeader(Period, Validity):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    donation_title = models.CharField(null=False, max_length=256)
    donation_minimum_amount = models.IntegerField(null=False, default=0)
    donation_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_donation_header"


class DonationDetail(models.Model):
    donation_header = models.ForeignKey(DonationHeader, null=False, on_delete=models.CASCADE)
    donation_description = models.CharField(null=False, max_length=256)
    donation_content = models.CharField(null=False, max_length=10240)
    donation_image = models.ImageField(null=False, blank=False, upload_to='DonationDetail/%Y/%m/%d')

    class Meta:
        db_table = "tbl_donation_detail"


class DonationInquiry(Period):
    donation_header = models.ForeignKey(DonationHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    donation_inquiry_type = models.CharField(null=False, max_length=10)
    donation_inquiry_content = models.CharField(null=False, max_length=1024)
    donation_inquiry_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_donation_inquiry"


class DonationInquiryAnswer(Period):
    donation_inquiry = models.ForeignKey(DonationInquiry, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    donation_inquiry_answer_content = models.CharField(null=False, max_length=1024)

    class Meta:
        db_table = "tbl_donation_inquiry_answer"


class DonationReply(Period):
    donation_header = models.ForeignKey(DonationHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    donation_reply_content = models.CharField(null=False, max_length=1024)
    donation_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_donation_reply"


class DonationDoner(models.Model):
    donation_header = models.ForeignKey(DonationHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    donate_amount = models.IntegerField(null=False, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_donation_doner"
