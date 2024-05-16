import boto3
import pyodbc
import os
import mysql

# Retrieve AWS credentials from environment variables
aws_access_key_id = os.environ.get('AKIATCKATAF2WQNNFK6N')
aws_secret_access_key = os.environ.get('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')
aws_region = os.environ.get('ap-south-1')

bucket_name = "task-bucket7385"
key = "Resume.pdf"
def read_data_from_s3(bucket_name, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=key)
    data = response['Body'].read().decode('utf-8')
    return data

def push_data_to_rds(data):
    db_host = os.environ['mydatabase.example.com']
    db_name = os.environ['db7385']
    db_user = os.environ['taskdb']
    db_password = os.environ['taskdb123']
    
    conn = mysql.connect(host="mydatabase.example.com", database="db7385", user="taskdb", password="taskdb123" )
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO data_table (data) VALUES (%s)"
            cursor.execute(sql, (data,))
        conn.commit()
    finally:
        conn.close()

def main():
    bucket_name = 'task-bucket7385'
    object_key = 'Resume.pdf' 

    data = read_data_from_s3(bucket_name,object_key)
    
    push_data_to_rds(data)
    
    print("Data successfully pushed to RDS database.")

if __name__ == "__main__":
    main()