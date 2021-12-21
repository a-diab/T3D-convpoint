import numpy as np

targets = np.load('L002.npy')
targets = targets[:,4]
print(targets)

predictions = np.load('L002pred.npy')
predictions = predictions[:,3]
print(predictions)

intersection = np.logical_and(targets, predictions)
OA = np.sum(intersection) / len(targets)
print(OA)

#road
target = targets.copy()
target[target!=1] = False
prediction = predictions.copy()
prediction[prediction!=1] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score1 = np.sum(intersection) / np.sum(union)
print(iou_score1)

#rdmarking
target = targets.copy()
target[target!=2] = False
prediction = predictions.copy()
prediction[prediction!=2] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score2 = np.sum(intersection) / np.sum(union)
print(iou_score2)

#natural
target = targets.copy()
target[target!=3] = False
prediction = predictions.copy()
prediction[prediction!=3] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score3 = np.sum(intersection) / np.sum(union)
print(iou_score3)

#building
target = targets.copy()
target[target!=4] = False
prediction = predictions.copy()
prediction[prediction!=4] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score4 = np.sum(intersection) / np.sum(union)
print(iou_score4)

#util
target = targets.copy()
target[target!=5] = False
prediction = predictions.copy()
prediction[prediction!=5] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score5 = np.sum(intersection) / np.sum(union)
print(iou_score5)

#pole
target = targets.copy()
target[target!=6] = False
prediction = predictions.copy()
prediction[prediction!=6] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score6 = np.sum(intersection) / np.sum(union)
print(iou_score6)

#car
target = targets.copy()
target[target!=7] = False
prediction = predictions.copy()
prediction[prediction!=7] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score7 = np.sum(intersection) / np.sum(union)
print(iou_score7)

#fence
target = targets.copy()
target[target!=8] = False
prediction = predictions.copy()
prediction[prediction!=8] = False
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score8 = np.sum(intersection) / np.sum(union)
print(iou_score8)

miou = (iou_score1 + iou_score2 + iou_score3 + iou_score4 + iou_score5 + iou_score6 + iou_score7 + iou_score8) / 8
print(miou)