from plyfile import PlyData, PlyElement
import numpy as np

plydata = PlyData.read("L002.ply")

x = plydata["vertex"].data["x"].astype(np.float32)-627567
y = plydata["vertex"].data["y"].astype(np.float32)-4842703
z = plydata["vertex"].data["z"].astype(np.float32)-80
reflectance = plydata["vertex"].data["scalar_Intensity"].astype(np.float32)-1
label = plydata["vertex"].data["scalar_Label"].astype(np.float32)
pts = np.concatenate([
        np.expand_dims(x,1),
        np.expand_dims(y,1),
        np.expand_dims(z,1),
        np.expand_dims(reflectance,1),
        np.expand_dims(label,1),
        ], axis=1).astype(np.float32)

mask = np.any(np.isnan(pts), axis=1)
#np.save(filename, arr[~mask])

pts = pts[~mask]

print(pts.shape)
print(pts)


np.save('L002.npy', pts)