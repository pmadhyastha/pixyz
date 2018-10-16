from .losses import Loss


class NLL(Loss):
    def __init__(self, p, input_var=[]):
        super(NLL, self).__init__(p, input_var=input_var)
        self.p = p

    def estimate(self, x, **kwargs):
        _x = super(NLL, self).estimate(x)
        nll = -self.p.log_likelihood(x)

        return nll
