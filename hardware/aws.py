import boto3, os

key_path = "./cctkey1.pem"
tag_name = {"Key": "Name", "Value": "halil-CA-server"}

client = boto3.client("ec2", region_name="eu-central-1")

reponse = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 20,
                'VolumeType': 'gp2'
            }
        },
    ],
    ImageId="ami-04e601abe3e1a910f",
    InstanceType="t2.micro",
    KeyName=os.path.basename(key_path).split('.')[0],
    SecurityGroups=['vpc-0525cb89b520dc144'],
    MaxCount=1,
    MinCount=1,
    UserData='''#!/bin/bash
    sudo apt update
    sudo apt install git
    sudo apt install python3
    sudo apt install python3-pip -y
    sudo pip install -U Flask
    
    ''',
    TagSpecifications=[{'ResourceType': 'instance', 'Tags': [tag_name]}]
)

inst_id = response['Instances'][0]['InstanceId']
print(inst_id)
