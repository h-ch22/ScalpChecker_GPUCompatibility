import tensorflow as tf
import os

if __name__ == '__main__':
    isGPUAvailable = len(tf.config.list_physical_devices('GPU')) > 0

    if isGPUAvailable:
        print("GPU Compatibility : Compatible.")

    else:
        print("GPU Compatibility : InCompatible.")