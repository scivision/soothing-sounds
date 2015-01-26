"""
forked from github.com/python-acoustics
GPLv3
"""

def ms(x):
    """Mean value of signal `x` squared.
    
    :param x: Dynamic quantity.
    :returns: Mean squared of `x`.
    
    """
    return (np.abs(x)**2.0).mean()
  
def rms(x):
    """Root mean squared of signal `x`.
    
    :param x: Dynamic quantity.
    
    .. math:: x_{rms} = lim_{T \\to \\infty} \\sqrt{\\frac{1}{T} \int_0^T |f(x)|^2 \\mathrm{d} t }
    
    :seealso: :func:`ms`.
    
    """
    return np.sqrt(ms(x))
    
def normalise(y, x=None):
    """Normalise power in y to a (standard normal) white noise signal.
    
    Optionally normalise to power in signal `x`.
    
    #The mean power of a Gaussian with :math:`\\mu=0` and :math:`\\sigma=1` is 1.
    """
    #return y * np.sqrt( (np.abs(x)**2.0).mean() / (np.abs(y)**2.0).mean() )
    if x is not None:
        x = ms(x)
    else:
        x = 1.0
    return y * np.sqrt( x / ms(y) )
    #return y * np.sqrt( 1.0 / (np.abs(y)**2.0).mean() )
    
    ## Broken? Caused correlation in auralizations....weird!
