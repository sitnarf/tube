from typing import Iterable
from matplotlib import pyplot
from tube.base.Block import Block
from tube.types.Dataset import Dataset


class PlotForecast(Block):
    def __init__(self, columns: Iterable[str], label: str = None):
        self.label = label
        self.columns = columns

    def execute(self, dataset: Dataset) -> Dataset:
        if self.label:
            pyplot.title(self.label)
        for column in self.columns:
            if column in dataset.data:
                pyplot.plot(dataset.data[column])
            if column in dataset.predict:
                pyplot.plot(dataset.predict[column])
        pyplot.show()
        return dataset
