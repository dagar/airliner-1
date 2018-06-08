def adder(*processes):
    return lambda *args, **kwargs: sum(p(*args, **kwargs) for p in processes)


def constant(value):
    return lambda *args, **kwargs: value


def integral(gain, t_sample, t_integral):
    """Generate an integral controller."""
    factor = gain * t_sample / t_integral

    def _integral():
        result = 0.0
        while True:
            current, target = yield result
            result += factor * (target - current)
    gen = _integral()
    next(gen)
    return lambda current, target: gen.send((current, target))


def limiter(min_val, max_val):
    return lambda val: max(min(val, max_val), min_val)


def proportional(gain, bias=0.0):
    return lambda current, target: gain * (target - current) + bias


def pi(p_gain, i_gain, t_sample, t_integral, p_bias=0.0):
    def _pi():
        p = proportional(p_gain, p_bias)
        i = integral(i_gain, t_sample, t_integral)
        p_out = i_out = 0.0
        while True:
            current, target = yield p_out + i_out
            p_out = p(current, target)
            i_out = i(0.0, p_out)
    gen = _pi()
    next(gen)
    return lambda current, target: gen.send((current, target))