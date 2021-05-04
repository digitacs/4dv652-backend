from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from models.regression.linear_regression import LinearRegression
from models.regression.random_forest import RandomForest
from models.classification.logistic_regression import LogisticRegression
from scores.models import Request
from scores.models import CamRequest
from scores.serializers import RequestSerializer
from scores.serializers import CamRequestSerializer
from scores.serializers import FrameSerializer

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from scores.functions import handle_video_upload  

from django.core.files.storage import FileSystemStorage
import mlflow
import gs
import google.cloud
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "mlflow-312506-6387830e8324.json"

class Version1(CreateAPIView):
    """
    Regression model: Linear Regression

    return: score
    """

    def create(self, request, *args, **kwargs):
        model = LinearRegression()
        score = model.predict(request.data)

        return Response({"score": score})


class Version2(CreateAPIView):
    """
    Regression model: Linear Regression
    Classification model: Logistic Regression

    return: score, weakest link
    """

    def create(self, request, *args, **kwargs):

        input_data = request.data
        if all(value == 0 for value in input_data.values()):
            return Response({'error': {
                'status': 400,
                'message': 'Input values must be larger than 0'
            }
            }, status=HTTP_400_BAD_REQUEST)

        try:
            regression_model = LinearRegression()
            score = regression_model.predict(input_data)
            classification_model = LogisticRegression()
            weakest_link = classification_model.predict(input_data)[0]
        except KeyError as error:
            return Response({'error': {
                'status': 400,
                'message': str(error)
            }
            }, status=HTTP_400_BAD_REQUEST)

        return Response({'score': score, 'weakest_link': weakest_link}, status=HTTP_200_OK)


class Version21(CreateAPIView):
    """
    Regression model: Random Forest
    Classification model: Logistic Regression

    return: score, weakest link
    """

    def create(self, request, *args, **kwargs):

        serializer_class = RequestSerializer()
        input_data = request.data
        if all(value == 0 for value in input_data.values()):
            return Response({'error': {
                'status': 400,
                'message': 'Input values must be larger than 0'
            }
            }, status=HTTP_400_BAD_REQUEST)

        try:
            regression_model = RandomForest()
            score = regression_model.predict(input_data)
            classification_model = LogisticRegression()
            weakest_link = classification_model.predict(input_data)[0]
        except ValueError:
            return Response({'error': {
                'status': 400,
                'message': 'Missing values'
            }
            }, status=HTTP_400_BAD_REQUEST)

        return Response({'score': score, 'weakest_link': weakest_link}, status=HTTP_200_OK)


class UploadFile(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Missing File")

        #f = request.data['file']
        file = request.FILES['file']
        #handle_video_upload(file)

        fs = FileSystemStorage()
        if fs.exists(file.name):
            fs.delete(file.name)
        file = fs.save(file.name, file)
        fileurl = fs.url(file)

        return Response({'file': 'http://rhtrv.com:8000'+fileurl},status=HTTP_201_CREATED)

class PoseNetFrames(ListCreateAPIView):

    serializer_class = FrameSerializer

    def create(self, request, *args, **kwargs):
        frames = []
        for i in request.data["frames"]:
            serializer = self.get_serializer(data=i, many=True)
            if serializer.is_valid():
                frames.append(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        """
        Uncomment to see what we get and what we are forwarding to mlflow.
        """
        #return Response({'file':frames}, status=HTTP_200_OK)


        try:
            kinect3D_model = mlflow.keras.load_model('gs://mlflow-atlas/mlflow_artifacts/0/cbca4a49c97a4f0a9e100a90658a5cb6/artifacts/kinect3D')
            predictions = kinect3D_model.predict(frames)
        except ValueError:
            return Response({'error': {
                'status': 400,
                'message': "Unable to handle prediction"
            }
            }, status=HTTP_400_BAD_REQUEST)

        return Response({'file':predictions}, status=HTTP_200_OK)


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
