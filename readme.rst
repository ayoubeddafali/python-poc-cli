POC Python CLI
=====================

A POC using python argparse module 


How to install
----------------

::

    $ pip install ck8s
    $ ck8s --help

Usage
------

First set the following env variables: 

- CK8S_PGP_FP
- CK8S_DEVBOX_VERSION
- CK8S_KUBESPRAY_REPOSITORY_PATH
- CK8S_CLOUD_PROVIDER
- CK8S_FLAVOR
- CK8S_OPS_REPOSITORY_PATH
- CK8S_CONFIG_PATH
- CK8S_ENVIRONMENT_NAME

And run :

::

    $ ck8s test sc ingress