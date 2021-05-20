from base.base_data_loader import BaseDataLoader
import tensorflow as tf
from sklearn.model_selection import train_test_split

class Dataloader(BaseDataLoader):
    def __init__(self, config, data_dir):
        super(Dataloader, self).__init__(config)
        self.data_dir = data_dir

    def preprocess(self, val_size=0.4, test_size=0.2):
        pass
