from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import PlanRequirement, RateRequirement, Requirement
from .serializer import PlanRequirementSerializer, RateRequirementSerializer, RatesRequirementSerializer, RequirementSerializer, RateWithRelatedDataSerializer
from products.models import Rate
from customers.models import Customer_type
import math
from datetime import datetime
from django.db.models import OuterRef, Subquery
from rest_framework import serializers
# Create your views here.
class RateWithRelatedDataSerializer(serializers.ModelSerializer):
    customer_type = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        fields = '__all__'

    def get_customer_type(self, obj):
        return Customer_type.objects.filter(raterequirement__rate=obj).distinct().values_list('name', flat=True)

    def get_requirements(self, obj):
        return Requirement.objects.filter(raterequirement__rate=obj).distinct().values_list('requirement_name', flat=True)


class RateWithRelatedDataView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateWithRelatedDataSerializer

class RateRequirement_Api(generics.GenericAPIView):
    serializer_class = RatesRequirementSerializer
    queryset = RateRequirement.objects.all()

    def get(self, request, *args, **kwargs):
        page_num = int(request.GET.get('page', 0))
        limit_num = int(request.GET.get('limit',10))
        start_num = (page_num) * limit_num
        end_num = limit_num * (page_num + 1)
        search_param = request.GET.get('search')
        raterequirements = RateRequirement.objects.all()
        total_raterequirements = raterequirements.count()
        if search_param:
            raterequirements = raterequirements.filter(requirement_icontains=search_param)
        serializer = self.serializer_class(raterequirements[start_num:end_num], many=True)
        return Response ({
            "status": "success",
            "total": total_raterequirements,
            "page": page_num,
            "last_page": math.ceil(total_raterequirements/ limit_num),
            "raterequirements": serializer.data
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"raterequirement": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message":serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
class RateRequirement_Detail(generics.GenericAPIView):
    queryset = RateRequirement.objects.all()
    serializer_class = RatesRequirementSerializer

    def get_raterequirement(self, request, pk, *args, **kw):
        try:
            return RateRequirement.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk, *args, **kw):
        raterequirement = self.get_raterequirement(pk=pk)
        if raterequirement == None:
            return Response({"status": "fail", "message": f"Rate requirement with id: {pk} not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(raterequirement)
        return Response({"status": "success", "data": {"raterequirement": serializer.data}}, status=status.HTTP_200_OK)
    def patch(self, request, pk, *args, **kw):
        raterequirement = self.get_raterequirement(pk)
        if raterequirement == None:
            return Response({"status": "fail", "message": f"Rate requirement with id: {pk} not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(raterequirement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data": {"raterequirement": serializer.data}}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
class All_Rates (generics.GenericAPIView):

    def get(self, request, *args, **kw):

        rates = Rate.objects.all()

        for rate in rates:
            print(rate.name)

        return HttpResponse("customers")

