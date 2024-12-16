from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status


# Create your views here.
class ProdcutListView(APIView):
    def get(self, request):
        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)


class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    def put(self, request, pk):
        try:
            items = Product.objects.get(pk=pk)
        except items.DoesNotExist:
            raise Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdcutDeleteView(APIView):
    def delete(self, request, pk):
        try:
            items = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        items.delete()
        return Response({"message": "Data deleted..."}, status=status.HTTP_200_OK)
