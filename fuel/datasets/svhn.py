# -*- coding: utf-8 -*-
import os

from fuel import config
from fuel.datasets import H5PYDataset
from fuel.transformers.defaults import uint8_pixels_to_floatX


class SVHN(H5PYDataset):
    """The Street View House Numbers (SVHN) dataset.

    SVHN [SVHN] is a real-world image dataset for developing machine
    learning and object recognition algorithms with minimal requirement
    on data preprocessing and formatting. It can be seen as similar in
    flavor to MNIST [LBBH] (e.g., the images are of small cropped
    digits), but incorporates an order of magnitude more labeled data
    (over 600,000 digit images) and comes from a significantly harder,
    unsolved, real world problem (recognizing digits and numbers in
    natural scene images). SVHN is obtained from house numbers in
    Google Street View images.

    .. [SVHN] Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco,
       Bo Wu, Andrew Y. Ng. *Reading Digits in Natural Images with
       Unsupervised Feature Learning*, NIPS Workshop on Deep Learning
       and Unsupervised Feature Learning, 2011.

    .. [LBBH] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner,
       *Gradient-based learning applied to document recognition*,
       Proceedings of the IEEE, November 1998, 86(11):2278-2324.

    Parameters
    ----------
    which_format : {1, 2}
        SVHN format 1 contains the full numbers, whereas SVHN format 2
        contains cropped digits.
    which_set : {'train', 'test', 'extra'}
        Whether to load the training set (73,257 examples), the test
        set (26,032 examples) or the extra set (531,131 examples).
        Note that SVHN does not have a validation set; usually you
        will create your own training/validation split
        using the `subset` argument.

    """
    filename = 'svhn_format_{}.hdf5'
    default_transformers = uint8_pixels_to_floatX(('features',))

    def __init__(self, which_format, which_set, **kwargs):
        self.which_format = which_format
        super(SVHN, self).__init__(self.data_path, which_set, **kwargs)

    @property
    def data_path(self):
        return os.path.join(
            config.data_path, self.filename.format(self.which_format))
