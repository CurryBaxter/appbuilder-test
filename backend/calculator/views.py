from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CalculationSerializer

@api_view(['POST'])
def calculate(request):
    serializer = CalculationSerializer(data=request.data)
    if serializer.is_valid():
        num1 = serializer.validated_data['num1']
        num2 = serializer.validated_data['num2']
        operation = serializer.validated_data['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            return Response({'error': 'Invalid operation'}, status=400)

        return Response({'result': result})
    else:
        return Response(serializer.errors, status=400)
