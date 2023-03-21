import time
import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from boto3.session import Session
import os


class Encoder:
    def __init__(self) -> None:
        self.PIPELINE_ID = settings.PIPELINE_ID
        self.OUTPUT_FILE_PREFIX = settings.OUTPUT_FILE_PREFIX
        
        

        self.CLIENT = boto3.client('elastictranscoder', 
            region_name='us-west-1', 
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        

    def create_job(self, input_file: str, output_file: dict):
        try:
            response = self.CLIENT.create_job(
                PipelineId=self.PIPELINE_ID, 
                Input={'Key': input_file}, 
                OutputKeyPrefix=self.OUTPUT_FILE_PREFIX, 
                Outputs=output_file
                )

        except ClientError as e:
            print(f'ERROR: {e}')
            return None

        return response['Job']

    def get_default_outputs(self, output_file: str):
        # To see a list of presets, head over to the AWS Elastic Transcoder page and select the Presets tab.
        outputs = [
            {
                'Key': output_file,
                'PresetId': '1351620000001-100190' # System preset: Full HD 1080i50 - MP4
            }
        ]
        return outputs


encoder = Encoder()

input_file = 'media/videos/Melody_Marks_2DHDlonger.mp4'
output_file = encoder.get_default_outputs('Melody_Marks_2DHDlonger_CONVERTED.mp4')

job = encoder.create_job(input_file=input_file, output_file=output_file)
print(job)