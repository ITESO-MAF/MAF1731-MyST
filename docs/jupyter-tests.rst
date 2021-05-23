
=============
Jupyter Tests
=============

This is a testS

$\sim \sum_{k=0}^{11}$

.. jupyter-execute::

    import numpy as np
    from matplotlib import pyplot as plt
    %matplotlib inline

    x = np.linspace(1E-3, 2 * np.pi)

    plt.plot(x, np.sin(x) / x)
    plt.plot(x, np.cos(x))
    plt.grid()



