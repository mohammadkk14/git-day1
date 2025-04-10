aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \  # Replace with your region's AMI ID
  --count 1 \
  --instance-type t2.micro \
  --key-name MyKeyPair \             # Replace with your key pair name
  --security-groups my-sg           # Replace with your security group name

