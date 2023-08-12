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
from bs4 import BeautifulSoup
from django.utils import timezone
import os
import boto3
from django.conf import settings

class RemoveContentFromTestHTML(APIView):
    def get(self, request):
        file_path = os.path.join("frontend/Html/test.html")
        
        # Check if the file exists
        if file_path:
            # Open the file in write mode to remove its content
            with open(file_path, "w") as file:
                file.truncate(0)  # Truncate the file to remove its content
            return Response({"message": "Content removed from the file."})
        else:
            return Response({"error": "File not found."}, status=404)
        

class nmap_api(APIView):
    
    def post(self, request):
        scan_type = request.data.get('scan_type')

        #Basic commands  [except excluding commands]
        if scan_type == 'Single target':
            ip = request.data.get('ip')
            result = subprocess.run(['sudo', 'nmap', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == 'Multiple_Targets':
            ip_addresses = request.data.get('ip')
            command = ['sudo', 'nmap'] + ip_addresses
            result =  subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "range of host":
            start_ip = request.data.get('start_ip')
            ip_count = int(request.data.get('ip_count'))
            start_ip_parts = start_ip.split('.')
            end_ip_parts = start_ip_parts[:-1] + [str(int(start_ip_parts[-1]) + ip_count - 1)]
            end_ip = '.'.join(end_ip_parts)
            ip_range = f"{start_ip}-{end_ip}"
            command = ['sudo', 'nmap'] + ip_range.split('-')
            result =  subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Entire Subnet":
            ip = request.data.get("ip")
            subnet = request.data.get('subnet')
            ip_range = f"{ip}/{subnet}"
            command = ['sudo', 'nmap', '-O', ip_range]
            print(command)
            result =  subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        # elif scan_type == "Random Hosts":
        #     num = request.data.get('number')
        #     # print(str(num))
            
        #     result =  subprocess.run(['sudo', 'namp', "-iR", "1"], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        #     # return Response("a")
        elif scan_type == "Aggressive Scan":
            ip = request.data.get('ip')
            print(ip)
            result =  subprocess.run(['sudo', 'nmap', '-A', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "IPv6":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-6', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        #Discovery
        elif scan_type == "Ping Only Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sP', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "NO Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PN', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP SYN Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PS', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP ACK Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PA', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "UDP Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PU', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "SCTP INIT Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PY', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "ICMP Echo Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PE', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "ICMP Timestamp Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PP', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "CMP Address Mask Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PM', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "IP Protocol Ping":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-PO', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Traceroute":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '--traceroute', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Force Reverse DNS Resolution":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-R', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Disable Reverse DNS Resolution":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-n', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Alternative DNS Lookup":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '--system-dns', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Manually Specify DNS Server":
            ip = request.data.get('ip')
            dns_ip = request.data.get('dns_ip')
            result =  subprocess.run(['sudo', 'nmap', '--dns-servers', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Create a Host List":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sL', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        #advanced

        elif scan_type == "TCP SYN Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sS', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP Connect Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sT', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "UDP Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sU', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP NULL Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sN', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP FIN Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sF', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Xmas Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sX', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "TCP ACK Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sA', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Custom TCP Scan":

            ip = request.data.get('ip')
            flag = request.data.get('flag')
            result =  subprocess.run(['sudo', 'nmap', '--scanflags',flag, ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "IP Protocol Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sO', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Send Raw Ethernet Packets":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '--send-eth', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Send IP Packets":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '--send-ip ', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        #port scanning


        elif scan_type == "Perform a Fast Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-F', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Scan Specific Ports":
            ip = request.data.get('ip')
            ports = request.data.get('ports')
            port_arg = '-p' + ports
            command = ['sudo', 'nmap', port_arg, ip]
            result =  subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Scan Ports by Name":
            ip = request.data.get('ip')
            ports = request.data.get('ports')
            port_arg = '-p' + ports
            command = ['sudo', 'nmap', port_arg, ip]
            result =  subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Scan Ports by TCP":
            ip = request.data.get('ip')
            tcp_ports = request.data.get('tcp_ports')
            if tcp_ports:
                tcp_port_arg = '-p T:' + tcp_ports
                tcp_command = ['sudo', 'nmap', '-sT', tcp_port_arg, ip]
                result = subprocess.run(tcp_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
                output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Scan Ports by UDP":
            ip = request.data.get('ip')
            udp_ports = request.data.get('udp_ports')
            if udp_ports:
                udp_port_arg = '-p U:' + udp_ports
                udp_command = ['sudo', 'nmap', '-sU', udp_port_arg, ip]
                result = subprocess.run(udp_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
                output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Scan All Ports":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-p', '*', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Scan Top Ports":
            ip = request.data.get('ip')
            num = request.data.get('number')
            result =  subprocess.run(['sudo', 'nmap', '--top-ports',num, ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Sequential Port Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-r', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        #Version Detection

        elif scan_type == "Operating System Detection":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-O', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Guess an Unknown OS":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-O','--osscan guess', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Service Version Detection":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sV', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Troubleshooting Version Scans":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sV','--version trace', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Perform a RPC Scan":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-sR', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        #Firewall Evasion Techniques except [Spoof MAC Address,Randomize Target Scan Order ,Zombie Scan]

        elif scan_type == "augment Packets":
            ip = request.data.get('ip')
            result =  subprocess.run(['sudo', 'nmap', '-f', ip], capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Pacify Specific MTU":
            ip = request.data.get('ip')
            mtu_value = request.data.get('mtu')
            mtu_command = ['sudo', 'nmap', '--mtu', str(mtu_value), ip]
            result = subprocess.run(mtu_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Use a Decoy":
            ip = request.data.get('ip')
            num = request.data.get('number')
            decoy_command = ['sudo', 'nmap', '-D', f'RND:{num}', ip]
            result = subprocess.run(decoy_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        # elif scan_type == "Zombie Scan":
        #     ip = request.data.get('ip')
        #     zombie = request.data.get('zombie')
        #     zombie_command = ['sudo', 'nmap', '-sI', zombie, ip]
        #     result = subprocess.run(zombie_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Manually Specify a Source Port":
            ip = request.data.get('ip')
            port = request.data.get('port')
            source_port_command = ['sudo', 'nmap', '--source-port', str(port), ip]
            result = subprocess.run(source_port_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Append Random Data":
            ip = request.data.get('ip')
            data_length = request.data.get('size')
            random_data_command = ['sudo', 'nmap', '--data-length', str(data_length), ip]
            result = subprocess.run(random_data_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        # elif scan_type == "Randomize Target Scan Order":
        #     ip = request.data.get('ip')
        #     randomize_command = ['sudo', 'nmap', '--randomize-hosts', ip]
        #     result = subprocess.run(randomize_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        # elif scan_type == "Spoof MAC Address":
        #     ip = request.data.get('ip')
        #     mac_address = request.data.get('MAC')
        #     spoof_mac_command = ['sudo', 'nmap', '--spoof-mac', mac_address, ip]
        #     result = subprocess.run(spoof_mac_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Send Bad Checksums":
            ip = request.data.get('ip')
            badsum_command = ['sudo', 'nmap', '--badsum', ip]
            result = subprocess.run(badsum_command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        #Troubleshooting And Debugging
        elif scan_type == "Getting Help":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '-h']
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)        

        elif scan_type == "Display Nmap Version":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '-V']
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        elif scan_type == "Verbose Output":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '-v',ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    

        elif scan_type == "Debugging":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '-d', ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    

        elif scan_type == "Display Port State Reason":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '-reason', ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        elif scan_type == "Trace Packets":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '--packet-trace', ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send) 

        elif scan_type == "Display Host Networking":
            ip = request.data.get('ip')
            command = ['sudo', 'nmap', '--iflist', ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        elif scan_type == "Display Port State Reason":
            ip = request.data.get('ip')
            interface = request.data.get('interface')
            command = ['sudo', 'nmap', '-e',interface, ip]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        # #NMAP Scripting Engine


        # elif scan_type == "Execute Individual Scripts":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  


        # elif scan_type == "Display Host Networking":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        # elif scan_type == "Display Host Networking":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        # elif scan_type == "Display Host Networking":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        # elif scan_type == "Display Host Networking":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        # elif scan_type == "Display Host Networking":
        #     ip = request.data.get('ip')
        #     command = ['sudo', 'nmap', '--iflist', ip]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)  

        else:
            return Response("Enter a valid Scan Type")
        
    
class volatality_api(APIView):
    
    def post(self, request):
        
        scan_type = request.data.get('scan_type')
        if scan_type == 'imageinfo':
            path = request.data.get('path')
            command = ['sudo', 'volatility', '-l', path, 'imageinfo']
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
    


class wireshark_api(APIView):
    
    def post (self,request):
        scan_type = request.data.get('scan_type')
        if scan_type == 'ifconfig':
            command = ['sudo', 'ifconfig']
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == 'capture the process':
            port = request.data.get('port')
            count = request.data.get('count')
            command = ['sudo', 'tshark', '-i', port, '-c', count]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == 'capture from specified interface':
            interface_number = request.data.get('interface_number')
            count = request.data.get('count')
            command = ['sudo', 'tshark', '-i', interface_number, '-c', count]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "capture packets from ports": #issue
            port = request.data.get('port')
            port_num = request.data.get('port_num')
            count = request.data.get('count')
            # display_filter = f'tcp.dstport == {port_num}'  # Use 'tcp.dstport' for TCP packets or 'udp.dstport' for UDP packets
            command = ['sudo', 'tshark', '-i', port, '-f', port_num, '-c', count]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "capture packet for duration":
            port = request.data.get('port')
            time = request.data.get('time')
            command = ['sudo', 'tshark', '-i', port, '-a', 'duration:'+time]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "capture packet for filesize":
            port = request.data.get('port')
            size = request.data.get('size')
            command = ['sudo', 'tshark', '-i', port, '-a', 'filesize:'+size]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        print("1")
        

class exiftool_api(APIView):
    
    def post(self,request):
        scan_type = request.data.get("scan_type")
        if scan_type == "Extract information from a file":
            location = request.data.get('location')
            command = ['sudo', "exiftool", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Print all meta information":
            location = request.data.get('location')
            command = ['sudo', "exiftool", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Print common meta information":
            location = request.data.get('location')
            command = ['sudo', "exiftool", "-common", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Find image size and exposure time":#
            location = request.data.get('location')
            command = ['sudo', "exiftool", "-s", "-ImageSize", "-ExposureTime", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        # elif scan_type == "Print formatted date/time for all JPG files in the current directory":#
        #     location = request.data.get('location')
        #     command = ['sudo', "exiftool", "-s", "-ImageSize", "-ExposureTime", location]
        #     result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
        #     output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Extract image resolution from EXIF IFD1":
            location = request.data.get('location')
            command = ['sudo', "exiftool", "-IFD1:XResolution", "-IFD1:YResolution", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "all author-related XMP information from an image":
            location = request.data.get('location')
            command = ['sudo', "exiftool", "-xmp:author:all", "-a", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Print one line of output containing the file name":
            location = request.data.get('location')
            command = ['sudo', "exiftool", '"$filename has date $dateTimeOriginal"', "-q", "-f", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "GPS positions from an AVCHD video":
            location = request.data.get('location')
            command = ['sudo', "exiftool", "-ee", "-p", '"$gpslatitude, $gpslongitude, $gpstimestamp"', location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)


class Strings_api(APIView):

    def post(self,request):
        scan_type = request.data.get('scan_type')

        if scan_type == "strings of printable characters in files":
            location = request.data.get('location')
            command = ['sudo', "strings", location]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "sequences that are at least 4 characters long":
            location = request.data.get('location')
            command = ['sudo', "strings","-n", "2", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Strings to also display the offsets":
            location = request.data.get('location')
            command = ['sudo', "strings", "-t", "d", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "may or may not scan the whole input file":
            location = request.data.get('location')
            command = ['sudo', "strings", "-a", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "strings of printable characters in files":
            location = request.data.get('location')
            command = ['sudo', "strings", "-d", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "separator used by Strings is a newline":
            location = request.data.get('location')
            command = ['sudo', "strings", "-s","[[[]]]", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
class Binwalk_api(APIView):
    def post(self,request):
        scan_type = request.data.get('scan_type')
        if scan_type == "basic scan on the specified file":
            location = request.data.get('location')
            command = ['sudo', "binwalk", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)   
         
        elif scan_type == "specific file signatures":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-S", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    
         
        elif scan_type == "recursive scan":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-r", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    
         
        elif scan_type == "entropy analysis":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-E", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    
         
        elif scan_type == "recursive signature scan":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-C", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)    
         
        elif scan_type == "only display results":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-q", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)     
         
        elif scan_type == "Extract and Display Disassembly":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-A", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)   
         
        elif scan_type == "Extract and Display Metadata":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-M", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)   
         
        elif scan_type == "Enable Debugging Output":
            location = request.data.get('location')
            command = ['sudo', "binwalk", "-d", location]
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        return Response("Not valid")  





class ProcessHTMLView(APIView):
    def get(self, request):
        file_path = os.path.join("frontend/Html/test.html")
        output_directory = os.path.join("Log")
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the content of the HTML file
            with open(file_path, "r") as file:
                html_content = file.read()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Format h2 tags as bold and p tags as normal text
            for h2_tag in soup.find_all("h2"):
                h2_tag.string = f"<b>{h2_tag.string}</b>"
            
            for p_tag in soup.find_all("p"):
                p_tag.unwrap()  # Remove the <p> tags, but retain the text and its formatting
            
            # Remove <br> tags
            for br_tag in soup.find_all("br"):
                br_tag.extract()

            # Generate the filename with the current timestamp
            timestamp = timezone.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_filename = f"{timestamp}.txt"
            output_file_path = os.path.join(output_directory, output_filename)

            # Save the processed content in a text file
            with open(output_file_path, "w") as output_file:
                output_file.write(str(soup))

            return Response({"message": f"HTML content processed and saved in {output_filename}."})
        else:
            return Response({"error": "File not found."}, status=404)

@api_view(['POST'])
def execute_command(request):
    command = request.data.get('command')
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return Response({'output': result})
    except subprocess.CalledProcessError as e:
        return Response({'output': f"Error: {e.output}"})


# @api_view(['POST'])
# def execute_command(request):
#     command = request.data.get('command')
#     try:
#         result = subprocess.check_output(command, shell=True, text=True)
#         output = {'output': result}
#     except subprocess.CalledProcessError as e:
#         output = {'output': f"Error: {e.output}"}

#     with open(os.path.join('frontend/Html/test.html'), 'a') as file:
#         file.write(f"<h2>{command}</h2>\n")
#         file.write(f"<p>{output['output']}</p>\n")

#     return Response({'output': result})


class Fsstat(APIView):
    def post(self, request):
        scan_type = request.data.get('scan_type')

        if scan_type == "Create image":
            location = request.data.get('location')
            save_name = request.data.get('save_name')
            command = ['sudo', "dd","if="+location,"of="+save_name, "bs=4M","status=progress"]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "Basic":
            location = request.data.get('location')
            command = ['sudo', "fsstat", location]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)
        
        elif scan_type == "Meta data of image":
            location = request.data.get('location')
            # command = ["sudo", "mmls", location]
            # print(command)
            # result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            
            command = ["sudo", "fls", "-r", location]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        elif scan_type == "hash value":
            alg = request.data.get("alg")
            name = request.data.get("name")
            command = ["sudo", "hashrat", "-"+alg, name]
            print(command)
            result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')
            output = result.stdout
            formatted_output = output.replace('\n', '<br>')
            with open(os.path.join('frontend/Html/test.html'), 'a') as file:
                file.write(f"<h2>{scan_type}</h2>\n")
                file.write(f"<p>{formatted_output}</p>\n")
            output_to_send = output.replace('\n', '')
            return Response(output_to_send)

        
        else:
            return Response("Stop")
        

        

class live_analysis(APIView):
    def post(self, request):
        scan_type = request.data.get('scan_type')

        if scan_type == "nmon":
            subprocess.run(['xterm', '-e', 'nmon'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return Response("Successful")
        elif scan_type == "testdisk":
            subprocess.run(['xterm', '-e', 'sudo', 'testdisk'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return Response("Successful")


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        
        s3 = boto3.client('s3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        
        bucket_name = 'your-bucket-name'
        s3.upload_fileobj(file, bucket_name, file.name)
        
        return render(request, 'upload_success.html')
    
    return render(request, 'upload_form.html')
