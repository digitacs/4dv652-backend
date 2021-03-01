from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from models.regression.linear_regression import LinearRegression
from models.classification.logistic_regression import LogisticRegression
from scores.models import Request
from scores.serializers import RequestSerializer


class Version1(CreateAPIView):
    def create(self, request, *args, **kwargs):
        model = LinearRegression()
        score = model.predict(request.data)

        return Response({"score": score})


class Version2(CreateAPIView):
    def create(self, request, *args, **kwargs):

        regression_model = LinearRegression()
        score = regression_model.predict(request.data)
        classification_model = LogisticRegression()
        weakest_link = classification_model.predict(request.data)[0]
        serializer_class = RequestSerializer()

        return Response({"score": score, "weakest_link": weakest_link})


def save_request(new_data, new_score):
    """
    Function to save the request as a new row in the database table.
    """
    new_r = Request

    new_r.No_1_Angle_Deviation = new_data.get("No_1_Angle_Deviation")
    new_r.No_2_Angle_Deviation = new_data.get("No_2_Angle_Deviation")
    new_r.No_3_Angle_Deviation = new_data.get("No_3_Angle_Deviation")
    new_r.No_4_Angle_Deviation = new_data.get("No_4_Angle_Deviation")
    new_r.No_5_Angle_Deviation = new_data.get("No_5_Angle_Deviation")
    new_r.No_6_Angle_Deviation = new_data.get("No_6_Angle_Deviation")
    new_r.No_7_Angle_Deviation = new_data.get("No_7_Angle_Deviation")
    new_r.No_8_Angle_Deviation = new_data.get("No_8_Angle_Deviation")
    new_r.No_9_Angle_Deviation = new_data.get("No_9_Angle_Deviation")
    new_r.No_10_Angle_Deviation = new_data.get("No_10_Angle_Deviation")
    new_r.No_11_Angle_Deviation = new_data.get("No_11_Angle_Deviation")
    new_r.No_12_Angle_Deviation = new_data.get("No_12_Angle_Deviation")
    new_r.No_13_Angle_Deviation = new_data.get("No_13_Angle_Deviation")
    new_r.No_1_NASM_Deviation = new_data.get("No_1_NASM_Deviation")
    new_r.No_2_NASM_Deviation = new_data.get("No_2_NASM_Deviation")
    new_r.No_3_NASM_Deviation = new_data.get("No_3_NASM_Deviation")
    new_r.No_4_NASM_Deviation = new_data.get("No_4_NASM_Deviation")
    new_r.No_5_NASM_Deviation = new_data.get("No_5_NASM_Deviation")
    new_r.No_6_NASM_Deviation = new_data.get("No_6_NASM_Deviation")
    new_r.No_7_NASM_Deviation = new_data.get("No_7_NASM_Deviation")
    new_r.No_8_NASM_Deviation = new_data.get("No_8_NASM_Deviation")
    new_r.No_9_NASM_Deviation = new_data.get("No_9_NASM_Deviation")
    new_r.No_10_NASM_Deviation = new_data.get("No_10_NASM_Deviation")
    new_r.No_11_NASM_Deviation = new_data.get("No_11_NASM_Deviation")
    new_r.No_12_NASM_Deviation = new_data.get("No_12_NASM_Deviation")
    new_r.No_13_NASM_Deviation = new_data.get("No_13_NASM_Deviation")
    new_r.No_14_NASM_Deviation = new_data.get("No_14_NASM_Deviation")
    new_r.No_15_NASM_Deviation = new_data.get("No_15_NASM_Deviation")
    new_r.No_16_NASM_Deviation = new_data.get("No_16_NASM_Deviation")
    new_r.No_17_NASM_Deviation = new_data.get("No_17_NASM_Deviation")
    new_r.No_18_NASM_Deviation = new_data.get("No_18_NASM_Deviation")
    new_r.No_19_NASM_Deviation = new_data.get("No_19_NASM_Deviation")
    new_r.No_20_NASM_Deviation = new_data.get("No_20_NASM_Deviation")
    new_r.No_21_NASM_Deviation = new_data.get("No_21_NASM_Deviation")
    new_r.No_22_NASM_Deviation = new_data.get("No_22_NASM_Deviation")
    new_r.No_23_NASM_Deviation = new_data.get("No_23_NASM_Deviation")
    new_r.No_24_NASM_Deviation = new_data.get("No_24_NASM_Deviation")
    new_r.No_25_NASM_Deviation = new_data.get("No_25_NASM_Deviation")
    new_r.No_1_Time_Deviation = new_data.get("No_1_Time_Deviation")
    new_r.No_2_Time_Deviation = new_data.get("No_2_Time_Deviation")
    new_r.score = new_score
