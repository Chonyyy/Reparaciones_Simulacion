import scipy.stats as stats

def P():
    """
    Genera un valor de una distribución Poisson con media  5.
    """
    return stats.poisson.rvs(mu=5, size=1)[0]

def E():
    """
    Genera un valor de una distribución exponencial con escala  1.
    """
    return stats.expon.rvs(scale=1, size=1)[0]

def N():
    """
    Genera un valor de una distribución normal con media  5 y desviación estándar  1.
    """
    return stats.norm.rvs(loc=5, scale=1, size=1)[0]

def B():
    """
    Genera un valor de una distribución binomial con n=10 y p=0.5.
    """
    return stats.binom.rvs(n=10, p=0.5, size=1)[0]

def G():
    """
    Genera un valor de una distribución gamma con parámetro de forma a=2 y escala  1.
    """
    return stats.gamma.rvs(a=2, scale=1, size=1)[0]

def U():
    """
    Genera un valor de una distribución uniforme con rango [0,  1].
    """
    return stats.uniform.rvs(loc=0, scale=1, size=1)[0]

def L():
    """
    Genera un valor de una distribución log-normal con parámetro de escala s=1 y escala  1.
    """
    return stats.lognorm.rvs(s=1, scale=1, size=1)[0]

def W():
    """
    Genera un valor de una distribución de Weibull con parámetro de forma c=1 y escala  1.
    """
    return stats.weibull_min.rvs(c=1, loc=0, scale=1, size=1)[0]
