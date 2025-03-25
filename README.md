# ENJOY
This is a revised version of pointops in [PointTransformer](https://github.com/POSTECH-CVLab/point-transformer/tree/master/lib/pointops "PointTransformer")

And the following issues are fixed.

https://github.com/huang-yh/GaussianFormer/issues/47

https://github.com/huang-yh/GaussianFormer/issues/49

https://github.com/huang-yh/GaussianFormer/issues/53

## The main changes are as follows:

``` bash
1. comment all #include <THC/THC.h>

2. add the import lines in \_\_init\_\_.py

3. change the setup.py, fix the issue that the setup.py cannot work in python environments, shown as "no module named pointops"
```

## How to use


``` bash

git clone https://github.com/xieyuser/pointops.git

cd pointops

python setup.py install

python

# note that, these is no need to import pointops, we do not need this.
import torch
import pointops_cuda
```

