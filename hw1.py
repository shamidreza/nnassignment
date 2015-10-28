
def load_data(dataset):
    # LOAD DATA #
    import os
    import cPickle
    import gzip

    # Download the MNIST dataset if it is not present
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory.
        new_path = os.path.join(
            os.path.split(__file__)[0],
            ".",
            ".",
            dataset
        )
        if os.path.isfile(new_path) or data_file == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        import urllib
        origin = (
            'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        )
        print 'Downloading data from %s' % origin
        urllib.urlretrieve(origin, dataset)

    print '... loading data'

    # Load the dataset
    print dataset
    f = gzip.open(dataset, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()

    def get_dataset(data_xy, train_xy, borrow=True):       
        data_x, data_y = data_xy
        data_x = data_x.reshape((data_x.shape[0], 28,28))
        data_y = data_x[:,:,14:].reshape((data_x.shape[0], 28*14))
        data_x = data_x[:,:,:14].reshape((data_x.shape[0], 28*14))
        t_x, t_y = train_xy
        t_x = t_x.reshape((t_x.shape[0], 28,28))
        t_y = t_x[:,:,14:].reshape((t_x.shape[0], 28*14))
        t_x = t_x[:,:,:14].reshape((t_x.shape[0], 28*14))
       
        return data_x, data_y

    
    train_set_x, train_set_y = get_dataset(train_set, train_set)
    test_set_x, test_set_y = get_dataset(test_set, train_set)
    valid_set_x, valid_set_y = get_dataset(valid_set, train_set)

    rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]
    return rval
    

def train(X, Y, hidden_layer_size, batch):
    # Please implement a two-layered neural network 
    # and train it using back-propagation
    # batch=True: batch backprop
    # batch=False: vanilla backprop
    # Please only use numpy and scipy packages
    raise NotImplementedError
    
def test(model, X):
    # please implement forward-pass to compute the output given the model and input
    raise NotImplementedError

if __name__ == '__main__':
    dataset = load_data('mnist.pkl.gz')
    print 'train input', dataset[0][0].shape
    print 'train output', dataset[0][1].shape
    print 'validation input', dataset[1][0].shape
    print 'validation output', dataset[1][1].shape
    print 'test input', dataset[2][0].shape
    print 'test output', dataset[2][1].shape
    
    model=train(X, Y, 500, True)
    Yh=test(model,X)
    
    # The goal is to implement a simple two-layer neural network and train it on the provided data 
    # 1- please implement the training/testing methods
    # 2- please visualize that your algorithm is working correctly
    # 3- please document the code itself and document using it for another developer
    # * feel free to change any part of this code to better match your program design
    
