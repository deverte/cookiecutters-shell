"""Preprocessing (normalization, vectorizing and etc.) and postprocessing data."""

import torch
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class Converter:
    """Preprocessor and postprocessor of the data for neural network.

    Attributes:
        scaler: Transform features by scaling each feature to a given range.
                Used for data normalization.
    """
    def __init__(self, feature_range=(-1, 1)):
        """Initialization of the Converter.

        Args:
            feature_range: Desired range of transformed data for MinMaxScaler. Default: (-1, 1).
        """
        self.scaler = MinMaxScaler(feature_range)

    def forward(self, train_data):
        """Forward transformation/conversion.

        Base function that contains all chain of forward transformation functions.
        Normalizes (scales) input data and transforms it into `torch.Tensor`.
        
        Args:
            train_data: Data that will be prepared to neural network.
        """
        forward_data = self.scale(train_data)
        forward_data = torch.FloatTensor(forward_data).view(-1)
        return forward_data

    def scale(self, train_data):
        """Scales input data.

        Args:
            train_data: Data to normalize.
        """
        scaled_data = self.scaler.fit_transform(train_data.reshape(-1, 1))
        return scaled_data

    def backward(self, output_data):
        """Backward transformation/conversion.

        Base function that contains all chain of backward transformation functions.
        Denormalizes input data.
        
        Args:
            output_data: Neural network output.
        """
        backward_data = self.unscale(output_data)
        return backward_data

    def unscale(self, output_data):
        """Scales input data back to the regular representation.

        Args:
            output_data: Data to be scaled back to the regular representation.
        """
        unscaled_data = self.scaler.inverse_transform(np.array(output_data).reshape(-1, 1))
        return unscaled_data