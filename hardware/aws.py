import boto3
import os

key_path = './cctkey1.pem'
sec_gr = 'sg-036cfa85ed283ecc7'
ami_id = 'ami-04e601abe3e1a910f'
region = 'eu-central-1'
tag_name = {"Key": "Name", "Value": "halil-CA-server"}

client = boto3.client('ec2', region_name=region)

response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 20,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=os.path.basename(key_path).split('.')[0],
    MaxCount=1,
    MinCount=1,
    UserData='''#!/bin/bash
    sudo apt update
    sudo apt install git -y
    sudo apt install python3 -y
    sudo apt install python3-pip -y
    sudo pip install -U Flask
    sudo pip install -U waitress
    cd /home/ubuntu
    git clone https://github.com/halilugur/CloudCA.git
    cd CloudCA
    python3 prod.py
    ''',
    Monitoring={
        'Enabled': False
    },
    SecurityGroupIds=[
        sec_gr,
    ],
    TagSpecifications=[{'ResourceType': 'instance', 'Tags': [tag_name]}]
)

inst_id = response['Instances'][0]['InstanceId']
print(inst_id)
