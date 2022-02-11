import os
import encryption as Encrypt

# Receiving the data into data.csv
# os.system('hadoop fs -get /tmp/data/data.csv data.csv')

# Encrypting the data with our script
Encrypt.encrypt('data.csv')

# Connecting in SSH with AWS ec2 instance, putting the file in home directory of ec2-user
os.system('scp -i mykeyBD.pem data.encrypted ec2-user@ec2-18-234-201-35.compute-1.amazonaws.com:~')