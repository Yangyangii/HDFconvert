from distutils.core import setup
 
setup (
        name               = 'HDFconvert',
        version             = '1.0.0',
        py_modules      = ['H5toImage'],
        author              = 'Yangyangii',
        author_email     = 'yjh2067@gmail.com',
        url                    = 'https://github.com/Yangyangii/HDFconvert',
        description        = 'To convert HDF format to other format files',
        install_requires = ['h5py'],
    )
