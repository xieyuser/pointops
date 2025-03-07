from setuptools import setup, find_packages  # ??find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
from distutils.sysconfig import get_config_vars

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

setup(
    name='pointops',
    version='0.1.0',
    author='Hengshuang Zhao',
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('pointops._C',
            [
                'src/pointops_api.cpp',
                'src/knnquery/knnquery_cuda.cpp',
                'src/knnquery/knnquery_cuda_kernel.cu',
                'src/sampling/sampling_cuda.cpp',
                'src/sampling/sampling_cuda_kernel.cu',
                'src/grouping/grouping_cuda.cpp',
                'src/grouping/grouping_cuda_kernel.cu',
                'src/interpolation/interpolation_cuda.cpp',
                'src/interpolation/interpolation_cuda_kernel.cu',
                'src/subtraction/subtraction_cuda.cpp',
                'src/subtraction/subtraction_cuda_kernel.cu',
                'src/aggregation/aggregation_cuda.cpp',
                'src/aggregation/aggregation_cuda_kernel.cu',
            ],
            extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O2']}
        )
    ],
    cmdclass={'build_ext': BuildExtension},
)

