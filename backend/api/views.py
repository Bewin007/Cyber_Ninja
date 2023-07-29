from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
import subprocess


class nmap_api(APIView):
    
    def post(self, request):
        scan_type = request.data.get('scan_type')
        a = ""

        if scan_type == 'Single target':
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == 'Multiple_Targets':
            ip_addresses = request.data.get('ip')
            command = ['sudo', 'nmap'] + ip_addresses
            a = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "range of host":
            start_ip = request.data.get('start_ip')
            ip_count = int(request.data.get('ip_count'))
            # Calculate the end IP address based on the start_ip and ip_count
            start_ip_parts = start_ip.split('.')
            end_ip_parts = start_ip_parts[:-1] + [str(int(start_ip_parts[-1]) + ip_count - 1)]
            end_ip = '.'.join(end_ip_parts)

            # Construct the IP range for the Nmap command
            ip_range = f"{start_ip}-{end_ip}"

            # Run the Nmap command with the IP range
            command = ['sudo', 'nmap'] + ip_range.split('-')
            a = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "Entire Subnet":
            start_ip = request.data.

        else:
            a = "error"
            return Response(a)