"""Some utils useful for neural network model development."""

# import pandas as pd
import torch
import plotly.graph_objects as go

def load_dataset(*args, **kwargs):
    """Loads dataset.

    Args:
        *args: `*args` description.
        **kwargs: `**kwargs` decription.
    
    Returns:
        List of raw data that can be splitted into `train` and `test`. For example:

        [112., 118., 132., 129., 121., 135., 148., 148., ..., 136.]
        
        Another example:

        [[1, 0], [2, 5], [5, 2], ..., [6, 8]]
    """
    # dataset = pd.read_csv(
    #     'some_file.dat', sep='\t', decimal=',', index_col=0, nrows=100,
    #     na_values='--', skiprows=lambda x: x in [0, 2]
    # )

    # return dataset
    assert False, '`utils.load_dataset` not implemented.'

def plot(*data):
    """Plots time series.

    Args:
        *data: `plotly` `graph_objects`. For example, `plotly.graph_objects.Scatter`.

    Example:
        utils.plot(go.Scatter(x=data.index, y=data['column_name']))
    """
    fig = go.Figure(
        data=data,
        layout={
            'title': {
                'text': 'Title'
            },
            'xaxis': {
                'title': {
                    'text': 'X Axis'
                }
            },
            'yaxis': {
                'title': {
                    'text': 'Y Axis'
                }
            }
        }
    )
    fig.show()

def plot_loss(*data):
    """Plots loss function.

    Args:
        *data: `plotly` `graph_objects`. For example, `plotly.graph_objects.Scatter`.

    Example:
        utils.plot(go.Scatter(x=epochs, y=loss))
    """
    fig = go.Figure(
        data=data,
        layout={
            'title': {
                'text': 'Loss'
            },
            'xaxis': {
                'title': {
                    'text': 'Epoch'
                }
            },
            'yaxis': {
                'title': {
                    'text': 'Loss'
                }
            }
        }
    )
    fig.show()

def split_train_test(data, test_data_size: int):
    """Splits data into train and test.

    Args:
        data: All data.
        test_data_size: Size of the `test` data.
                        Size of the `train` will be `len(data) - test_data_size`.
    """
    train_data = data[:-test_data_size]
    test_data = data[-test_data_size:]

    return train_data, test_data

def create_inout_sequences(input_data, train_window_size: int):
    """Forms data with labels that will be used for model training.

    Forms data with labels that will be used for model training.
    Label is the next element after window.
    Output organized with the following format (data = input_data):
    [[data[0 : train_window_size], data[train_window_size : train_window_size + 1]],
     [data[1 : 1 + train_window_size], data[1 + train_window_size : 1 + train_window_size + 1]],
     ...
     [data[i : i + train_window_size], data[i + train_window_size : i + train_window_size + 1]],
     ...]
    Or briefly:
    [[data_0, label], ...]

    Args:
        input_data: Data that will be used for training.
        train_window_size: Size of the window for the training.
    
    Returns:
        Data for training with labels. For example, we have this data with window size = 3:

        [112., 118., 132., 129., 121., 135., 148., 148., ..., 136.]
        
        Return will be:

        [[[112., 118., 132.], [129.]],
         [[118., 132., 129.], [121.]],
         ...]
    """
    inout_seq = []
    L = len(input_data)
    for i in range(L - train_window_size):
        train_seq = input_data[i : i + train_window_size]
        train_label = input_data[i + train_window_size : i + train_window_size + 1]
        inout_seq.append((train_seq, train_label))
    return inout_seq

def train_model(model, device, train_inout_seq, loss_function, optimizer, epochs=150):
    """Trains the model.

    Args:
        model: Model to train.
        device: Device on which a `torch.Tensor` is or will be allocated.
        train_inout_seq: Sequence of data and labels in format [[data_0, label], ...].
                         See `create_inout_sequences` function.
        loss_function: Loss function. See https://pytorch.org/docs/stable/nn.html#loss-functions.
        optimizer: Optimizer. See https://pytorch.org/docs/stable/optim.html#algorithms.
        epochs: Number of epochs. Default: 150.
    """
    epoch_list = []
    loss_list = []

    for i in range(epochs):
        for seq, labels in train_inout_seq:
            optimizer.zero_grad()
            model.hidden_cell = (
                torch.zeros(1, 1, model.hidden_size).to(device),
                torch.zeros(1, 1, model.hidden_size).to(device)
            )

            y_pred = model(seq.to(device))

            single_loss = loss_function(y_pred, labels.to(device))
            single_loss.backward()
            optimizer.step()

        epoch_list.append(i)
        loss_list.append(single_loss.item())

        if i % 25 == 1:
            print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

    print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')
    return epoch_list, loss_list