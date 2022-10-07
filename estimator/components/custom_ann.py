from annoy import AnnoyIndex
from typing import Literal
import json


class CustomAnnoy(AnnoyIndex):
    """
    Inherits AnnoyIndex: The save and load functions have been modified according to the website needs.
    """
    def __init__(self, f: int, metric: Literal["angular", "euclidean", "manhattan", "hamming", "dot"]):
        super().__init__(f, metric)
        self.label = []

    # noinspection PyMethodOverriding
    def add_item(self, i: int, vector, label: str) -> None:
        super().add_item(i, vector)
        self.label.append(label)

    def get_nns_by_vector(self, vector, n: int, search_k: int = ..., include_distances: Literal[False] = ...):
        indexes = super().get_nns_by_vector(vector, n)
        labels = [self.label[link] for link in indexes]
        return labels

    def load(self, fn: str, prefault: bool = ...):
        """
        Responsible for loading .ann and .json files saved by save method.
        """
        super().load(fn)
        path = fn.replace(".ann", ".json")
        self.label = json.load(open(path, "r"))

    def save(self, fn: str, prefault: bool = ...):
        """
        Responsible for Saving .ann and .json files.
        """
        super().save(fn)
        path = fn.replace(".ann", ".json")
        json.dump(self.label, open(path, "w"))
