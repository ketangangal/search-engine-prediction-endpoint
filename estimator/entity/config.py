import os
from from_root import from_root


class AwsStorage:
    def __init__(self):
        self.ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
        self.SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
        self.REGION_NAME = os.environ["AWS_REGION"]
        self.BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]
        self.KEY = "model"
        self.ZIP_NAME = "model/artifacts.tar.gz"
        self.ARTIFACTS_ROOT = os.path.join(from_root(), "artifacts")
        self.ARTIFACTS_PATH = os.path.join(from_root(), "artifacts", "artifacts.tar.gz")

    def get_aws_storage_config(self):
        return self.__dict__


# Label Should Update from MongoDb
class PredictConfig:
    def __init__(self):
        self.LABEL = 101
        self.REPOSITORY = 'pytorch/vision:v0.10.0'
        self.BASE_MODEL = 'resnet18'
        self.PRETRAINED = True
        self.IMAGE_SIZE = 256
        self.EMBEDDINGS_LENGTH = 256
        self.SEARCH_MATRIX = 'euclidean'
        self.NUMBER_OF_PREDICTIONS = 20
        self.STORE_PATH = os.path.join(from_root(), "artifacts")
        self.MODEL_PATHS = [(os.path.join(from_root(), "artifacts", "embeddings.ann"), "embeddings.ann"),
                            (os.path.join(from_root(), "artifacts", "model.pth"), "model.pth")]

    def get_pipeline_config(self):
        return self.__dict__
