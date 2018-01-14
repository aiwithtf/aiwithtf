from distutils.version import LooseVersion

TF_VERSION_MIN = '1.1'


def log(message):
    print(message)


def check_tf(tf_):
    error_message = "Please use TensorFlow {} or later".format(TF_VERSION_MIN)
    tf_version = tf_.__version__
    condition = LooseVersion(tf_version) > LooseVersion(TF_VERSION_MIN)
    assert condition, error_message
    log('Using TensorFlow {}'.format(tf_version))
