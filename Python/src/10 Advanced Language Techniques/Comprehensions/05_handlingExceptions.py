def catch(fn, handle=lambda e : e, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return handle(e)

# create a list containing zero
numbers = [float(n) for n in range(-5, 5)]

# comprehension will raise an exception for a zero entry
reciprocals = [catch(lambda : 1/n) for n in numbers]
print reciprocals
