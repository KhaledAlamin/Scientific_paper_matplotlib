# plot.py
import matplotlib.pyplot as plt

def show_plot():    
    plt.plot([1, 2, 3], [4, 5, 3])


# test.py
from unittest import mock

@mock.patch('scientific_papdder_matplotlib.SPPlot.Plot')
def test_show_plot(mock_plt):
    show_plot()
    mock_plt.plot.assert_called_once_with([1, 2, 3], [4, 5, 3])