"""PyTorch neural network module and functions for working with it."""

import torch
import torch.nn as nn

class LSTM(nn.Module):
    """LSTM-based PyTorch neural network module.

    Attributes:
        hidden_size: The number of features in the hidden state h.
        lstm: LSTM layer.
        linear: Linear layer.
        hidden_cell: Hidden cell for LSTM.
    """
    def __init__(self, input_size=1, hidden_size=100, out_features=1):
        """Initialization of module.

        Args:
            input_size: The number of expected features in the input x. Default: 1.
            hidden_size: The number of features in the hidden state h. Default: 100.
            out_features: Size of each output sample. Default: 1.
        """
        super().__init__()
        self.hidden_size = hidden_size

        self.lstm = nn.LSTM(input_size, hidden_size)

        self.linear = nn.Linear(hidden_size, out_features)

        self.hidden_cell = (
            torch.zeros(1, 1, self.hidden_size),
            torch.zeros(1, 1, self.hidden_size)
        )

    def forward(self, input_seq):
        """Forward pass.

        Defines the computation performed at every call.

        Args:
            input_seq: Input sequence `torch.Tensor`.
        """
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq), 1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

def predict(model, device, test_inputs, future_predictions_size: int, train_window_size: int):
    """Prediction based on model.

    Args:
        model: Already trainded model.
        device: Device on which a `torch.Tensor` is or will be allocated.
        test_inputs: Input sequence.
        future_predictions_size: Size of the predictions.
        train_window_size: Size of the window.
    """
    predictions = test_inputs.copy()

    for i in range(future_predictions_size):
        seq = torch.FloatTensor(predictions[-train_window_size:]).to(device)
        with torch.no_grad():
            model.hidden = (
                torch.zeros(1, 1, model.hidden_size).to(device),
                torch.zeros(1, 1, model.hidden_size).to(device)
            )
            predictions.append(model(seq).item())

    predictions = predictions[-train_window_size:]
    
    return predictions