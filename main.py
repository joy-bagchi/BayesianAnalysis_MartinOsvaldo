from multiprocessing import freeze_support

import pymc as pm
import arviz as az
from matplotlib import pyplot as plt


def model():
    with pm.Model() as first_model:
        theta = pm.Beta('theta', alpha=1, beta=1)
        y = pm.Binomial('y', n=1, p=theta, observed=1)
        trace = pm.sample(1000)
    az.plot_trace(trace)
    plt.show()
    # az.plot_posterior(trace)
    # az.summary(trace)


if __name__ == '__main__':
    freeze_support()
    model()
