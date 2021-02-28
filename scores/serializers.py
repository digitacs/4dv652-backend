from rest_framework import serializers
from scores.models import LRRequest


class LRRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LRRequest
        fields = (
            'Id',
            'No_1_Angle_Deviation',
            'No_2_Angle_Deviation',
            'No_3_Angle_Deviation',
            'No_4_Angle_Deviation',
            'No_5_Angle_Deviation',
            'No_6_Angle_Deviation',
            'No_7_Angle_Deviation',
            'No_8_Angle_Deviation',
            'No_9_Angle_Deviation',
            'No_10_Angle_Deviation',
            'No_11_Angle_Deviation',
            'No_12_Angle_Deviation',
            'No_13_Angle_Deviation',
            'No_1_NASM_Deviation',
            'No_2_NASM_Deviation',
            'No_3_NASM_Deviation',
            'No_4_NASM_Deviation',
            'No_5_NASM_Deviation',
            'No_6_NASM_Deviation',
            'No_7_NASM_Deviation',
            'No_8_NASM_Deviation',
            'No_9_NASM_Deviation',
            'No_10_NASM_Deviation',
            'No_11_NASM_Deviation',
            'No_12_NASM_Deviation',
            'No_13_NASM_Deviation',
            'No_14_NASM_Deviation',
            'No_15_NASM_Deviation',
            'No_16_NASM_Deviation',
            'No_17_NASM_Deviation',
            'No_18_NASM_Deviation',
            'No_19_NASM_Deviation',
            'No_20_NASM_Deviation',
            'No_21_NASM_Deviation',
            'No_22_NASM_Deviation',
            'No_23_NASM_Deviation',
            'No_24_NASM_Deviation',
            'No_25_NASM_Deviation',
            'No_1_Time_Deviation',
            'No_2_Time_Deviation',
            'score'
        )
