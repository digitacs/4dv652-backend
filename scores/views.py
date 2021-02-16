from rest_framework import views
from rest_framework.response import Response

from models.regression.linear_regression import LinearRegression
from scores.serializers import LRRequestSerializer
from scores.models import LRRequest


class PredictView(views.APIView):
    def post(self, request, format=None):
        model = LinearRegression()
        score = model.predict(request.data)

        r = LRRequest()

        r.No_1_Angle_Deviation = request.data.get("No_1_Angle_Deviation")
        r.No_2_Angle_Deviation = request.data.get("No_2_Angle_Deviation")
        r.No_3_Angle_Deviation = request.data.get("No_3_Angle_Deviation")
        r.No_4_Angle_Deviation = request.data.get("No_4_Angle_Deviation")
        r.No_5_Angle_Deviation = request.data.get("No_5_Angle_Deviation")
        r.No_6_Angle_Deviation = request.data.get("No_6_Angle_Deviation")
        r.No_7_Angle_Deviation = request.data.get("No_7_Angle_Deviation")
        r.No_8_Angle_Deviation = request.data.get("No_8_Angle_Deviation")
        r.No_9_Angle_Deviation = request.data.get("No_9_Angle_Deviation")
        r.No_10_Angle_Deviation = request.data.get("No_10_Angle_Deviation")
        r.No_11_Angle_Deviation = request.data.get("No_11_Angle_Deviation")
        r.No_12_Angle_Deviation = request.data.get("No_12_Angle_Deviation")
        r.No_13_Angle_Deviation = request.data.get("No_13_Angle_Deviation")
        r.No_1_NASM_Deviation = request.data.get("No_1_NASM_Deviation")
        r.No_2_NASM_Deviation = request.data.get("No_2_NASM_Deviation")
        r.No_3_NASM_Deviation = request.data.get("No_3_NASM_Deviation")
        r.No_4_NASM_Deviation = request.data.get("No_4_NASM_Deviation")
        r.No_5_NASM_Deviation = request.data.get("No_5_NASM_Deviation")
        r.No_6_NASM_Deviation = request.data.get("No_6_NASM_Deviation")
        r.No_7_NASM_Deviation = request.data.get("No_7_NASM_Deviation")
        r.No_8_NASM_Deviation = request.data.get("No_8_NASM_Deviation")
        r.No_9_NASM_Deviation = request.data.get("No_9_NASM_Deviation")
        r.No_10_NASM_Deviation = request.data.get("No_10_NASM_Deviation")
        r.No_11_NASM_Deviation = request.data.get("No_11_NASM_Deviation")
        r.No_12_NASM_Deviation = request.data.get("No_12_NASM_Deviation")
        r.No_13_NASM_Deviation = request.data.get("No_13_NASM_Deviation")
        r.No_14_NASM_Deviation = request.data.get("No_14_NASM_Deviation")
        r.No_15_NASM_Deviation = request.data.get("No_15_NASM_Deviation")
        r.No_16_NASM_Deviation = request.data.get("No_16_NASM_Deviation")
        r.No_17_NASM_Deviation = request.data.get("No_17_NASM_Deviation")
        r.No_18_NASM_Deviation = request.data.get("No_18_NASM_Deviation")
        r.No_19_NASM_Deviation = request.data.get("No_19_NASM_Deviation")
        r.No_20_NASM_Deviation = request.data.get("No_20_NASM_Deviation")
        r.No_21_NASM_Deviation = request.data.get("No_21_NASM_Deviation")
        r.No_22_NASM_Deviation = request.data.get("No_22_NASM_Deviation")
        r.No_23_NASM_Deviation = request.data.get("No_23_NASM_Deviation")
        r.No_24_NASM_Deviation = request.data.get("No_24_NASM_Deviation")
        r.No_25_NASM_Deviation = request.data.get("No_25_NASM_Deviation")
        r.No_1_Time_Deviation = request.data.get("No_1_Time_Deviation")
        r.No_2_Time_Deviation = request.data.get("No_2_Time_Deviation")
        r.score = score[0]

        # r.save()

        return Response({"score": score})
