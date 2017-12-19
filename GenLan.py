from osgeo import gdal
import numpy as np
from scipy.io import loadmat
import argparse

__version__ = "0.1.0"
#out_image1=loadmat('PaviaU.mat')['paviaU']#340,610,103
#out_image1=loadmat('Salinas.mat')['salinas']       #217,512,224
#out_image1=loadmat('Indian_pines.mat')['indian_pines']#145,145,220
#out_image1=loadmat('CupriteS1_F224.mat')#
#print(out_image1)


def mat2lan(filepath):
    
    a=filepath.find('.')
    filename=filepath[0:a]
  
    input_image1=loadmat(filepath)
    
    a=np.asarray([1,2,3])
    key=''
    for i in input_image1.keys():
        if(type(input_image1[i])==type(a)):
            key=i
            break
        
    input_image2=input_image1[key]#340,610,103
    
    driver = gdal.GetDriver(89)
    driver.Register()
    str=filename+'.lan'
    
    arr=np.asarray(input_image2.shape, np.int32)
   
    data=  driver.Create(str,int(arr[1]),int(arr[0]),int(arr[2]),gdal.GDT_Int16)
    
    out_image1=loadmat(filepath)[key]#340,610,103
    
    for i in range(data.RasterCount):
        band = data.GetRasterBand(i+1)
        a=out_image1[:,:,i]
        band.WriteArray(a,0,0)

    print("Finish")


def get_parser():

    parser = argparse.ArgumentParser(
        description='Query words meanings via the command line')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
                        help='the words to meanings')
    parser.add_argument('-v', '--version', action='store_true',
                        help='displays the current version of youdao')
    return parser



def command_line_runner():
  
    parser = get_parser()
    args = vars(parser.parse_args())
    
    if args['version']:
        print(__version__)
        return

    if not args['query']:
        parser.print_help()
        return
    
    mat2lan(" ".join(args['query']))
    
    
if __name__=='__main__':
    command_line_runner()


