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

        #Basic commands  [except excluding commands]
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
            ip = request.data.get("ip")
            subnet = request.data.get('subnet')
            ip_range = f"{ip}/{subnet}"
            command = ['sudo', 'nmap', '-O', ip_range]
            a = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        # elif scan_type == "Random Hosts":
        #     num = request.data.get('number')
        #     # print(str(num))
            
        #     a = subprocess.run(['sudo', 'namp', "-iR", "1"], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     return Response(a.stdout)
        #     # return Response("a")
        elif scan_type == "Aggressive Scan":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-A', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "IPv6":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-6', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        #Discovery
        elif scan_type == "Ping Only Scan":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-sP', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "NO Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PN', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "TCP SYN Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PS', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "TCP ACK Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PA', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "UDP Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PU', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "SCTP INIT Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PY', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "ICMP Echo Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PE', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "ICMP Timestamp Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PP', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "CMP Address Mask Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PM', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        elif scan_type == "IP Protocol Ping":
            ip = request.data.get('ip')
            a = subprocess.run(['sudo', 'nmap', '-PO', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            return Response(a.stdout)

        

        else:
            a = "error"
            return Response(a)