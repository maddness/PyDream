def fail_proof(fn, times=3):
    def wrapper(*args, **kwargs):
        for i in range(times):
            try:
                return fn(*args, **kwargs)
            except NameError:
                print 'failed miserably...'
        return 'Retry max count reached.'

    return wrapper


@fail_proof
def good_one():
    return str


@fail_proof
def gonna_fail():
    raise NameError('Not so fast...')


# old style
fail_safe = fail_proof(gonna_fail, 3)
print fail_safe()

# cool style
print gonna_fail()
