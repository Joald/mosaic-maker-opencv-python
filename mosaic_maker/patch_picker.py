import cv2
from config import SET_DESCRIPTION_CSV_FILE_NAME, \
    MAX_ACCEPTED_MIN_HISTOGRAM_DISTANCE, PATCH_SIZE, \
    USE_SOBEL_DESCRIPTOR, USE_HISTOGRAM_DESCRIPTOR, HISTOGRAM_VECTOR_LENGTH
import numpy as np

from mosaic_maker.patch import Patch


class PatchPicker:
    def __init__(self, set_name, set_path):
        self.set_name = set_name
        self.set_path = set_path

        self.patches = self._load_patches()

    def _load_patches(self):
        (patches_dict, sobel_patches_dict) = self._load_patches_images()
        descriptions_dict = self._load_csv()

        patches_list = []

        for patch_name in descriptions_dict.keys():
            patches_list.append(Patch(patch_name,
                                      patches_dict[patch_name], sobel_patches_dict[patch_name],
                                      descriptions_dict[patch_name]))

        return np.array(patches_list)

    def _load_patches_images(self):
        patches_path = self.set_path / 'images'
        sobel_patches_path = self.set_path / 'sobel-images'

        patches_dict = {}
        sobel_patches_dict = {}

        for patch_path in patches_path.iterdir():
            patch_name = patch_path.name

            if patch_name.startswith('.'):
                continue

            patches_dict[patch_name] = cv2.imread(patch_path.as_posix())
            sobel_patches_dict[patch_name] = cv2.imread((sobel_patches_path / patch_name).as_posix(), cv2.IMREAD_GRAYSCALE)

        return patches_dict, sobel_patches_dict

    def _load_csv(self):
        descriptions_dict = {}

        csv_path = self.set_path / SET_DESCRIPTION_CSV_FILE_NAME

        with open(csv_path) as csv_file:
            for row in csv_file:
                first_comma = row.find(',')
                file_name = row[:first_comma]
                features_string = row[first_comma + 1:]
                features = np.fromstring(features_string, sep=',', dtype=np.float32)
                descriptions_dict[file_name] = features

            csv_file.close()

        return descriptions_dict

    def pick_patch_for(self, target_patch):
        sobel_distances = np.array([], np.float32)
        histogram_distances = np.array([], np.float32)

        for patch in self.patches:
            if USE_SOBEL_DESCRIPTOR:
                # ToDo extract sobel part of patches features

                # ToDo compare both vectors - what metric seems good for this end?
                # https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

                sobel_distances = np.append(sobel_distances, 0)

            if USE_HISTOGRAM_DESCRIPTOR:
                # ToDo extract histogram part of patches features - what metric works best?
                # https://docs.opencv.org/3.3.0/d6/dc7/group__imgproc__hist.html
                # https://docs.opencv.org/3.3.0/d6/dc7/group__imgproc__hist.html#gaf4190090efa5c47cb367cf97a9a519bd

                # ToDo compare awesome opencv compare hist implementation with one written by yourself
                histogram_distances = np.append(histogram_distances, 0)

        if not USE_SOBEL_DESCRIPTOR:
            # ToDo get best patch index based on sobel distances
            # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.argmin.html
            best_patch_index = 0
        elif not USE_HISTOGRAM_DESCRIPTOR:
            # ToDo get best patch index based on histogram distances
            # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.argmin.html
            best_patch_index = 0
        else:
            # ToDo combine sobel and histogram information
            # https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#normalize
            # https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
            # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.where.html
            best_patch_index = 0

        return self.patches[best_patch_index]
