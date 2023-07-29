import subprocess

try:
    ip_addresses = ['192.168.1.131', '192.168.1.10']

    # Construct the nmap command with the target IP addresses using sudo
    command = ['sudo', 'nmap', '-O'] + ip_addresses

    # Run the nmap command
    result = subprocess.run(command, capture_output=True, text=True, check=True, input='root@2004\n', encoding='utf-8')

    # Print the output
    print(result.stdout)
except subprocess.CalledProcessError as e:
    # If there is an error, print the error message
    print("Error:", e)
