from estimator.entity.config import AwsStorage
import tarfile
from boto3 import Session
import os


class StorageConnection:
    """
    Created connection with S3 bucket using boto3 api to fetch the model from Repository.
    """
    def __init__(self):
        self.config = AwsStorage()
        self.session = Session(aws_access_key_id=self.config.ACCESS_KEY_ID,
                               aws_secret_access_key=self.config.SECRET_KEY,
                               region_name=self.config.REGION_NAME)
        self.s3 = self.session.resource("s3")
        self.bucket = self.s3.Bucket(self.config.BUCKET_NAME)

    def get_package_from_testing(self):
        print("Fetching Artifacts From S3 Bucket .....")
        if os.path.exists(self.config.ARTIFACTS_ROOT + "embeddings.ann"):
            os.remove(self.config.ARTIFACTS_ROOT + "embeddings.ann")

        if os.path.exists(self.config.ARTIFACTS_ROOT + "model.pth"):
            os.remove(self.config.ARTIFACTS_ROOT + "model.pth")

        if os.path.exists(self.config.ARTIFACTS_ROOT + "embeddings.json"):
            os.remove(self.config.ARTIFACTS_ROOT + "embeddings.json")

        self.bucket.download_file(self.config.ZIP_NAME, self.config.ARTIFACTS_PATH)
        folder = tarfile.open(self.config.ARTIFACTS_PATH)
        folder.extractall(self.config.ARTIFACTS_ROOT)
        folder.close()
        os.remove(self.config.ARTIFACTS_PATH)
        print("Fetching Completed !")


if __name__ == "__main__":
    connection = StorageConnection()
    connection.get_package_from_testing()
