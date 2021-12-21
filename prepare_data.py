import argparse
import os
from plyfile import PlyData, PlyElement
import numpy as np
from sklearn.decomposition import PCA

parser = argparse.ArgumentParser()
parser.add_argument("--rootdir", type=str, required=True)
parser.add_argument("--destdir", type=str, required=True)
parser.add_argument("--test", action="store_true")
args = parser.parse_args()

# create the directory
train_filenames = ["L001.ply",  "L003.ply",  "L004.ply"]
test_filenames = ["L002.ply"]

if args.test:
    filenames = test_filenames
    save_dir = os.path.join(args.destdir,"test_pointclouds")
else:
    filenames = train_filenames
    save_dir = os.path.join(args.destdir,"train_pointclouds")
os.makedirs(save_dir, exist_ok=True)

for filename in filenames:
    if args.test:
        fname = os.path.join(args.rootdir, "test_data", filename)
    else:
        fname = os.path.join(args.rootdir, "train_data", filename)
    print(fname)
    plydata = PlyData.read(fname)
    print(plydata)
    x = plydata["vertex"].data["x"].astype(np.float32)-627567
    y = plydata["vertex"].data["y"].astype(np.float32)-4842703
    z = plydata["vertex"].data["z"].astype(np.float32)-80
    reflectance = plydata["vertex"].data["scalar_Intensity"].astype(np.float32)-1
    if not args.test:
        label = plydata["vertex"].data["scalar_Label"].astype(np.float32)

    if args.test:
        pts = np.concatenate([
                np.expand_dims(x,1),
                np.expand_dims(y,1),
                np.expand_dims(z,1),
                np.expand_dims(reflectance,1),
                ], axis=1).astype(np.float32)

        np.save(os.path.join(save_dir, os.path.splitext(filename)[0]), pts)

    else:
        pts = np.concatenate([
                np.expand_dims(x,1),
                np.expand_dims(y,1),
                np.expand_dims(z,1),
                np.expand_dims(reflectance,1),
                np.expand_dims(label,1),
                ], axis=1).astype(np.float32)

        pca = PCA(n_components=1)
        pca.fit(pts[::10,:2])
        pts_new = pca.transform(pts[:,:2])
        hist, edges = np.histogram(pts_new, pts_new.shape[0]// 2500000)

        count = 0

        for i in range(1,edges.shape[0]):
            mask = np.logical_and(pts_new<=edges[i], pts_new>edges[i-1])[:,0]
            np.save(os.path.join(save_dir, os.path.splitext(filename)[0]+f"_{count}"), pts[mask])
            count+=1

        try:
            hist, edges = np.histogram(pts_new, pts_new.shape[0]// 2500000 -2, range=[(edges[1]+edges[0])//2,(edges[-1]+edges[-2])//2])
        except:
            print("zero bins exception")

        for i in range(1,edges.shape[0]):
            mask = np.logical_and(pts_new<=edges[i], pts_new>edges[i-1])[:,0]
            np.save(os.path.join(save_dir, os.path.splitext(filename)[0]+f"_{count}"), pts[mask])
            count+=1