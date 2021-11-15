_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_2x.py',
    '../_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1,)))
checkpoint_config = dict(interval=3)

classes = ('drone',)
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=2,
    train=dict(
        img_prefix='data/mav-vid/images/',
        classes=classes,
        ann_file='data/mav-vid/train.json'),
    val=dict(
        img_prefix='data/mav-vid/images/',
        classes=classes,
        ann_file='data/mav-vid/val.json'),
    test=dict(
        img_prefix='data/mav-vid/images/',
        classes=classes,
        ann_file='data/mav-vid/val.json'))

load_from = 'checkpoints/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth'
optimizer = dict(lr=0.001)