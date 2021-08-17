.. _Course_Introduction:

===================
Course Introduction
===================

:math:`\alpha_{t=1}`: just a greek letter

:math:`\text{This is an inline math} \sim \sum_{k=0}^{11}`

.. math::
    J(w)=-\frac{1}{m} \sum_{i=1}^{m} \big[ y_i\ log(p_{i}) + (1-y_{i})\ log(1-p_{i}) \big]

.. jupyter-execute::

    import numpy as np
    from matplotlib import pyplot as plt
    %matplotlib inline

    x = np.linspace(1E-3, 2 * np.pi)

    plt.plot(x, np.sin(x) / x)
    plt.plot(x, np.cos(x))
    plt.grid()
