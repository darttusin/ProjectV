import tensorflow as tf

from core.yolov4 import YOLO, decode, filter_boxes
import core.utils as utils
from core.config import cfg

WEIGHTS='./data/yolov4.weights'
OUTPUT='./checkpoints/yolov4-416'
TINY=False
INPUT_SIZE=416
SCORE_THRES=0.2
FRAMEWORK='tf'
MODEL='yolov4'

def save_tf():
  STRIDES, ANCHORS, NUM_CLASS, XYSCALE = utils.load_config()

  input_layer = tf.keras.layers.Input([INPUT_SIZE, INPUT_SIZE, 3])
  feature_maps = YOLO(input_layer, NUM_CLASS, MODEL, TINY)
  bbox_tensors = []
  prob_tensors = []
  if TINY:
    for i, fm in enumerate(feature_maps):
      if i == 0:
        output_tensors = decode(fm,  INPUT_SIZE // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FRAMEWORK)
      else:
        output_tensors = decode(fm, INPUT_SIZE // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FRAMEWORK)
      bbox_tensors.append(output_tensors[0])
      prob_tensors.append(output_tensors[1])
  else:
    for i, fm in enumerate(feature_maps):
      if i == 0:
        output_tensors = decode(fm, INPUT_SIZE // 8, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FRAMEWORK)
      elif i == 1:
        output_tensors = decode(fm, INPUT_SIZE // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FRAMEWORK)
      else:
        output_tensors = decode(fm, INPUT_SIZE // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FRAMEWORK)
      bbox_tensors.append(output_tensors[0])
      prob_tensors.append(output_tensors[1])
  pred_bbox = tf.concat(bbox_tensors, axis=1)
  pred_prob = tf.concat(prob_tensors, axis=1)
  if FRAMEWORK == 'tflite':
    pred = (pred_bbox, pred_prob)
  else:
    boxes, pred_conf = filter_boxes(pred_bbox, pred_prob, score_threshold=SCORE_THRES, input_shape=tf.constant([INPUT_SIZE, INPUT_SIZE]))
    pred = tf.concat([boxes, pred_conf], axis=-1)
  model = tf.keras.Model(input_layer, pred)
  utils.load_weights(model, WEIGHTS, MODEL, TINY)
  model.summary()
  model.save(OUTPUT)

if __name__ == '__main__':
    try:
        save_tf()
    except SystemExit:
        pass
