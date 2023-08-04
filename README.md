# T3D-convpoint
Testing ConvPoint on Toronto-3D

These scripts are mostly based on the example models used on Paris-Lille dataset from the ConvPoint github but modified to fit the Toronto-3D dataset plus some metric calculations.

## Data processing
Run prepare_data.py to process the Toronto-3D .ply files to the same format used by Convpoint. They will be split and converted to numpy.

For the training set:
```
python prepare_data.py --rootdir path_to_data --destdir path_to_data_processed
```
For the test set:
```
python prepare_data.py --rootdir path_to_data --destdir path_to_data_processed --test
```
## Training
```
python t3d_seg.py --rootdir path_to_data_dir --savedir path_to_save_dir
```

To train without lidar intensity:
```
python t3d_seg.py --rootdir path_to_data_dir --savedir path_to_save_dir --nocolor
```

## Testing

```
python t3d_seg.py --rootdir path_to_data_dir --savedir path_to_save_dir --test
```

If the model was trained without using the lidar intensity:
```
python t3d_seg.py --rootdir path_to_data_dir --savedir path_to_save_dir --test --nocolor
```

## Metrics

Run the metrics.py script to the calculate the OA, mIOU, and IOU for each class

