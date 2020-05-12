# pytorch-lstm-time-series

---

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Documentation](#Documentation)
    1. [Requirements](#Requirements)
    2. [Project structure](#Project-structure)
    3. [LSTM example](#LSTM-example)
4. [Author](#Author)
5. [License](#License)

---


## About
LSTM neural network time series prediction [Cookiecutter](https://cookiecutter.readthedocs.io/) template for [PyTorch](https://pytorch.org/) machine learning framework.
Killer feature of this template is convenient model development and easy adaptation for software thanks to separation of model and the functionality of data preparation.

In most cases it is necessary to implement **only one** function for building a working model. But, of course, this model will require improvements for optimization, accuracy and etc.

Inspired by [Usman Malik](https://twitter.com/usman_malikk)'s article [Time Series Prediction using LSTM with PyTorch in Python](https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python/).

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:pytorch-lstm-time-series
```

**Usage**  
```sh
cc z:pytorch-lstm-time-series
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**model_name**: lstm - Name of the `LSTM`-based model.  


---


## Documentation
### Requirements
- [Python](https://www.python.org/)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [PyTorch](https://pytorch.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NumPy](https://numpy.org/) (*optional*)
- [Pandas](http://pandas.pydata.org/) (*optional*)
- [Plotly](https://plotly.com/python/) (*optional*)
- [seaborn](https://seaborn.pydata.org/) (*optional*)


### Project structure
This `Cookiecutter` template provides the following project structure.

**{{cookiecutter.model_name}}.ipynb**  
Main file for model creation and testing. [***only for model development***]

**conversion.py**  
`Python` module with `Converter` class for pre- and post-processing data (normalization, vectorizing and etc.). [***for model and software development***]

**model.py**  
File with LSTM-based model and functions connected with trained model (for example, prediction of future values). [***for model and software development***]

**utils.py**  
`Python` module with useful utils for data manipulation, plotting, training model. [***only for model development***]


### LSTM example
#### Loading a Dataset
Let's assume that we want to solve the problem of predicting the number of passengers at the airport.
For convenience, we can use already existing datasets. One of these datasets is contained in the seaborn library. It's called `'flights'`.

Let's create project from cookiecutter and call it `myLSTM` (you can call it somehow different).

First, we need to import some modules.

`myLSTM.ipynb`  
```python
%load_ext autoreload
%autoreload 2

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import plotly.graph_objects as go
# User modules
import utils
import model as ml
from conversion import Converter
```

Now we can decide what device will be used for `torch.Tensor` computation.
There is default algorithm for device selection. Device will be cuda if available.

```python
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
device.type
```

Next step is to load data.  
We need to edit `load_dataset` function inside the `utils.py` file.

`utils.py`  
```python
import seaborn as sns

def load_dataset(*args, **kwargs):
    """<docstring>"""
    dataset = sns.load_dataset("flights")
    return dataset
```

And now we can execute loader block.

`myLSTM.ipynb`  
```python
dataset = utils.load_dataset()
```

After that we can plot our data.

`myLSTM.ipynb`  
```python
utils.plot(go.Scatter(x=dataset.index, y=dataset['passengers'].values.astype('float')))
```

#### Preparing a Data
Next, we need to prepare our data as input for neural network.

First, we should set up `Converter` object (`conversion.py` module) that will be used for data normalization, vectorization and etc.  
This class has `__init__` function that used for initializing the main properties of conversion and two base functions - `forward` and `backward`.  
The `forward` function is needed to prepare data for entering the neural network (normalization, vectorizing and etc.).  
The `backward` function is needed to represent output data as our regular data (inverse transformation of `forward`).  
These two functions, for convenience, may depend on other functions that make more specific conversions. For example, `forward` function may depend on `scale` function, and `backward` on `unscale`. You can freely add new functions or change these functions to fit your aim, but the main input and output should be inside `forward` and `backward`.

For our aim it is good to scale data in (-1, 1) range. And we can leave `Converter` without changes.

`myLSTM.ipynb`  
```python
converter = Converter(feature_range=(-1, 1))
```

It is good to split our data to train and test. We have only 144 values (each month during 12 years). And, for example, let's select the data for the last year as test data. Also if it's needed you can change `split_train_test` function inside `utils.py` module.

`myLSTM.ipynb`  
```python
TEST_DATA_SIZE: int = 12

train_data, test_data = utils.split_train_test(
    dataset['passengers'].values.astype('float'),
    TEST_DATA_SIZE
)
```

Now we can normalize data with our `Converter`.

`myLSTM.ipynb`  
```python
train_data_normalized = converter.forward(train_data)
```

We have periodic data and it is good to set our window size as `12` and set label as the next element after window (you can customize this function - `create_inout_sequences` inside `utils.py` module).

`myLSTM.ipynb`  
```python
TRAIN_WINDOW_SIZE: int = 12

train_inout_seq = utils.create_inout_sequences(train_data_normalized, TRAIN_WINDOW_SIZE)
```

#### Model Creation
Inside the `model.py` file it is LSTM-based model with [LSTM](https://pytorch.org/docs/stable/nn.html#lstm) and [Linear](https://pytorch.org/docs/stable/nn.html#linear) layer. You can customise this model for improving efficiency.

We just load model with squared L2 norm ([MSELoss](https://pytorch.org/docs/stable/nn.html#mseloss)) as loss function and [Adam](https://pytorch.org/docs/stable/optim.html#torch.optim.Adam) as optimizer (you can choose another or create your own) with `learning rate = 0.001`.

`myLSTM.ipynb`  
```python
model = ml.LSTM().to(device)
loss_function = nn.MSELoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

#### Model Training
Now we can train the model, for example, with `150` epochs.

`myLSTM.ipynb`  
```python
epochs, loss = utils.train_model(model, device, train_inout_seq, loss_function, optimizer, epochs=150)
```

Also we can plot losses.

`myLSTM.ipynb`  
```python
utils.plot_loss(go.Scatter(x=epochs, y=loss))
```

#### Predictions
After training we can predict future! Or not? Let's check this.

For example, we want to predict the number of flights over the next 12 months.

`myLSTM.ipynb`  
```python
FUTURE_PREDICTIONS_SIZE: int = 12

test_inputs = train_data_normalized[-TRAIN_WINDOW_SIZE:].tolist()
```

Let's switch the model to evaluation mode, predict desired values and transform this values to our regular data.

`myLSTM.ipynb`  
```python
model.eval()

predictions = ml.predict(
    model, device, test_inputs, future_predictions_size=FUTURE_PREDICTIONS_SIZE,
    train_window_size=TRAIN_WINDOW_SIZE
)

predictions = converter.backward(predictions)
```

And we can plot our result.

`myLSTM.ipynb`  
```python
utils.plot(
    go.Scatter(x=dataset.index, y=dataset['passengers']),
    go.Scatter(x=dataset.index[-FUTURE_PREDICTIONS_SIZE:], y=predictions.flatten()),
)
```

#### Saving a Model
After training we can save model's weights for using it, for example, in enterprise.

`myLSTM.ipynb`  
```python
torch.save(model.state_dict(), 'model.pth')
```


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License

[MIT](/LICENSE)