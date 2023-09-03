from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import  CreateAPIView

from .serializers import HistoryTransfer,HistoryTransferSerializer
from apps.transfer.models import Username