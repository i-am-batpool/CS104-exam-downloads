import numpy as np
def dists(spicepoints):
    spicepoints1=spicepoints.reshape(1,spicepoints.shape[0],2)
    spicepoints2=spicepoints.reshape(spicepoints.shape[0],1,2)
    dists=np.linalg.norm((spicepoints1-spicepoints2), axis=2)
    return dists
def a(spicepoints, centers, labels):
    dist=dists(spicepoints)
    mask = (labels==labels[:,None]) #v.v.v.imp 
    count=np.sum(mask, axis=1)-1
    count = np.where(count == 0, 1, count)
    dast=dist/count
    ret = (mask @ dast)
    retur = np.diagonal(ret)
    return retur

def b(spicepoints, centers, labels):
    redata=spicepoints.reshape(spicepoints.shape[0],1,2)
    recenters=centers.reshape(1,centers.shape[0],2)
    distann=np.linalg.norm(redata-recenters, axis=2)
    newlabels=np.argsort(distann, axis=1)[:,1] #really imp method...getting index of second smallest element for each row
    dist=dists(spicepoints)
    mask=(labels==newlabels[:,None])
    count=np.sum(mask, axis=1)-1
    count = np.where(count == 0, 1, count)
    dast=dist/count[:,None]
    ret = (mask @ dast)
    retur = np.diagonal(ret)
    print(retur)
    return retur

spice=np.array([[1,1],[2,1],[3,2],[4,5],[6,9]])
center=np.array([[0,0],[1,1]])
labels=np.array([0,1,1,0,0])
b(spice,center,labels)