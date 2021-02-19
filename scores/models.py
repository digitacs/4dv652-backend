import uuid
from django.db import models


class LRRequest(models.Model):
    '''
    The LRRequest keep information about all requests to the ML Linear Regression algorithm.

    Attributes:
        Id: Unique Id to identify requests.
        created_at: The date when request was created.
        score: The response of the ML algorithm: a score of how good the movement was.
    '''
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    aimoscore = models.DecimalField(
        null=True, blank=True, max_digits=25, decimal_places=24)
    No_1_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_2_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_3_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_4_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_5_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_6_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_7_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_8_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_9_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_10_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_11_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_12_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_13_Angle_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_1_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_2_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_3_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_4_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_5_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_6_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_7_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_8_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_9_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_10_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_11_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_12_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_13_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_14_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_15_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_16_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_17_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_18_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_19_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_20_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_21_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_22_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_23_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_24_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_25_NASM_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_1_Time_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    No_2_Time_Deviation = models.DecimalField(
        max_digits=25, decimal_places=24)
    estimatedscore = models.DecimalField(
        null=True, blank=True, max_digits=25, decimal_places=24)
    score = models.DecimalField(max_digits=25, decimal_places=24)
    patient_id = models.CharField(max_length=200, default="0")
