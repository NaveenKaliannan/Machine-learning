
import numpy as np

## reading all the lines at once line = f.readlines(), list(f)
## reading line by line f.readline()
data=[]
data = np.loadtxt("/home/naveenk/temp/del/OOdistance/purewater", dtype='float')
print(" Dimension = {}, shape = {} ".format(data.ndim,data.shape))
nrow,ncolomn=data.shape

print("without transpposing = {} {} {}".format(np.dot(data[:, 0], data[:, 2]), np.dot(data[:, 0], data[:, 3]), np.dot(data[:, 0], data[:, 5]) ) )

data=np.matrix.flatten(data)
data = data.reshape(nrow,ncolomn)

data=np.array(data)
data=np.transpose(data)
print("without transpposing = {} {} {} ".format(np.dot(data[0, :], data[2, :]), np.dot(data[0, :], data[3, :]), np.dot(data[0, :], data[5, :]) ) )
