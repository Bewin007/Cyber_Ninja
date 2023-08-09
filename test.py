import paramiko

def upload_file(local_path, remote_path, hostname, username, private_key_path):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

    ssh_client.connect(hostname=hostname, username=username, pkey=private_key)

    sftp = ssh_client.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()

    ssh_client.close()

if __name__ == "__main__":
    local_file_path = "/home/bewin/Desktop/Cyber_Ninja_Backend/Log/2023-08-03_18-22-13.txt"
    remote_file_path = "/file.txt"
    lightsail_hostname = "lightsail.aws.amazon.com"
    lightsail_username = "vkt"
    private_key_path = "/home/bewin/Desktop/Cyber_Ninja_Backend/key.pem"

    upload_file(local_file_path, remote_file_path, lightsail_hostname, lightsail_username, private_key_path)


