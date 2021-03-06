import functools
import operator
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
IMAGES_SET = 'test'
TARGET_IMAGE = 'test-target.jpg'

# ToDo set better parameters values

PATCH_SIZE = 32

SOBEL_BLUR_KERNEL_SHAPE = (21, 21)
EDGES_LOWER_THRESHOLD = 0

HISTOGRAM_GRID_SHAPE = (1, 1)
HISTOGRAM_BUCKETS = (1, 1, 1)
HISTOGRAM_VECTOR_LENGTH = functools.reduce(operator.mul, HISTOGRAM_GRID_SHAPE, 1) \
                          * functools.reduce(operator.mul, HISTOGRAM_BUCKETS, 1)

MAX_ACCEPTED_MIN_HISTOGRAM_DISTANCE = 0.9

USE_SOBEL_DESCRIPTOR = True
USE_HISTOGRAM_DESCRIPTOR = True

SET_DESCRIPTION_CSV_FILE_NAME = 'set-description.csv'

assert PATCH_SIZE % HISTOGRAM_GRID_SHAPE[0] == 0 and PATCH_SIZE % HISTOGRAM_GRID_SHAPE[1] == 0,\
    'HISTOGRAM_GRID_SHAPE dimensions have to be divisors of the PATCH_SIZE'
