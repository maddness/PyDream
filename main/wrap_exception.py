def fail_proof(fn, times=1):
    def wrapper(*args, **kwargs):
        for i in range(times):
            try:
                return fn(*args, **kwargs)
            except NameError:
                print 'failed miserably...'
        return 'Retry max count reached.'

    return wrapper


def good_one(a):
    return str


@good_one
def gonna_fail():
    raise NameError('Not so fast...')


# fail_safe = fail_proof(gonna_fail, 3)
print gonna_fail()

# try_me()
