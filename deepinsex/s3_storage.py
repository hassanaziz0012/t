from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


# We'll be using the following custom storage classes to store our data in the S3 bucket.
class StaticStorage(S3Boto3Storage):
    location = settings.AWS_LOCATION
    default_acl = settings.AWS_DEFAULT_ACL


class PublicMediaStorage(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = settings.AWS_DEFAULT_ACL
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False