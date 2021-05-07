# import boto3

# ACCESS_KEY = '#'
# SECRET_KEY = '#'

# def upload_file(file_name, bucket):
#     """
#     Function to upload a file to an S3 bucket
#     """
#     object_name = file_name
#     s3_client = boto3.client('s3' , aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY )
#     response = s3_client.upload_file(file_name, bucket, object_name)

#     return response


# def download_file(file_name, bucket):
#     """
#     Function to download a given file from an S3 bucket
#     """
#     s3 = boto3.resource('s3',  aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY )
#     output = f"downloads/{file_name}"
#     s3.Bucket(bucket).download_file(file_name, output)

#     return output


# def list_files(bucket):
#     """
#     Function to list files in a given S3 bucket
#     """
#     print("yeah")
#     s3 = boto3.client('s3',  aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY )
#     contents = []
#     try:
#         for item in s3.list_objects(Bucket=bucket)['Contents']:
#             print(item)
#             contents.append(item)
#     except Exception as e:
#         pass

#     return contents
