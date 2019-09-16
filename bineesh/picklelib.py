import pickle


def dump(data, filename):
    """ data:  any python object
    filename: string
    returns: None
    """
    with open(filename, 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def load(filename):
    """
    filename: string
    returns: python object or None
    """
    with open(filename, 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        data = pickle.load(f)
        return data
