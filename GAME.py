import pygame
import os
import math

# -------------------
# Initialization
# -------------------
pygame.init()
try:
    pygame.mixer.init()
    music_available = True
except pygame.error:
    music_available = False
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# -------------------
# Data & Assets
# -------------------
PLATFORM_DATA = [
    {
        "start": 0.943,
        "end": 2.308,
        "y": 260
    },
    {
        "start": 2.774,
        "end": 2.889,
        "y": 260
    },
    {
        "start": 3.104,
        "end": 3.204,
        "y": 260
    },
    {
        "start": 3.404,
        "end": 3.506,
        "y": 260
    },
    {
        "start": 3.708,
        "end": 3.811,
        "y": 260
    },
    {
        "start": 4.029,
        "end": 4.695,
        "y": 260
    },
    {
        "start": 5.294,
        "end": 5.391,
        "y": 260
    },
    {
        "start": 5.592,
        "end": 5.674,
        "y": 260
    },
    {
        "start": 5.905,
        "end": 5.989,
        "y": 260
    },
    {
        "start": 6.222,
        "end": 6.305,
        "y": 260
    },
    {
        "start": 6.544,
        "end": 7.187,
        "y": 260
    },
    {
        "start": 7.8,
        "end": 7.899,
        "y": 260
    },
    {
        "start": 8.133,
        "end": 8.201,
        "y": 260
    },
    {
        "start": 8.462,
        "end": 8.526,
        "y": 170
    },
    {
        "start": 8.757,
        "end": 8.856,
        "y": 170
    },
    {
        "start": 10.341,
        "end": 10.457,
        "y": 260
    },
    {
        "start": 10.656,
        "end": 10.785,
        "y": 260
    },
    {
        "start": 11.0,
        "end": 11.162,
        "y": 170
    },
    {
        "start": 11.314,
        "end": 11.43,
        "y": 80
    },
    {
        "start": 12.831,
        "end": 12.964,
        "y": 260
    },
    {
        "start": 13.179,
        "end": 13.295,
        "y": 170
    },
    {
        "start": 13.495,
        "end": 13.595,
        "y": 80
    },
    {
        "start": 13.761,
        "end": 13.894,
        "y": 260
    },
    {
        "start": 14.107,
        "end": 14.205,
        "y": 170
    },
    {
        "start": 14.449,
        "end": 14.551,
        "y": 80
    },
    {
        "start": 14.749,
        "end": 14.882,
        "y": 260
    },
    {
        "start": 15.077,
        "end": 15.209,
        "y": 170
    },
    {
        "start": 15.389,
        "end": 15.554,
        "y": 80
    },
    {
        "start": 15.687,
        "end": 15.801,
        "y": 260
    },
    {
        "start": 16.033,
        "end": 16.166,
        "y": 170
    },
    {
        "start": 16.347,
        "end": 16.412,
        "y": 80
    },
    {
        "start": 17.917,
        "end": 18.066,
        "y": 260
    },
    {
        "start": 18.246,
        "end": 18.345,
        "y": 170
    },
    {
        "start": 18.558,
        "end": 18.656,
        "y": 80
    },
    {
        "start": 18.856,
        "end": 19.037,
        "y": 340
    },
    {
        "start": 19.173,
        "end": 19.306,
        "y": 260
    },
    {
        "start": 19.49,
        "end": 19.606,
        "y": 170
    },
    {
        "start": 19.802,
        "end": 19.917,
        "y": 80
    },
    {
        "start": 20.116,
        "end": 20.264,
        "y": 340
    },
    {
        "start": 20.485,
        "end": 20.783,
        "y": 260
    },
    {
        "start": 20.783,
        "end": 20.899,
        "y": 170
    },
    {
        "start": 21.132,
        "end": 21.246,
        "y": 80
    },
    {
        "start": 21.413,
        "end": 21.546,
        "y": 340
    },
    {
        "start": 21.71,
        "end": 22.179,
        "y": 260
    },
    {
        "start": 21.963,
        "end": 22.36,
        "y": 170
    },
    {
        "start": 22.36,
        "end": 22.67,
        "y": 80
    },
    {
        "start": 22.67,
        "end": 22.904,
        "y": 340
    },
    {
        "start": 22.936,
        "end": 23.773,
        "y": 260
    },
    {
        "start": 23.593,
        "end": 23.888,
        "y": 80
    },
    {
        "start": 23.263,
        "end": 23.904,
        "y": 170
    },
    {
        "start": 23.888,
        "end": 24.235,
        "y": 340
    },
    {
        "start": 24.202,
        "end": 24.809,
        "y": 260
    },
    {
        "start": 24.53,
        "end": 24.826,
        "y": 170
    },
    {
        "start": 24.843,
        "end": 25.179,
        "y": 80
    },
    {
        "start": 25.179,
        "end": 25.408,
        "y": 340
    },
    {
        "start": 25.49,
        "end": 25.808,
        "y": 260
    },
    {
        "start": 25.791,
        "end": 26.139,
        "y": 170
    },
    {
        "start": 26.106,
        "end": 26.45,
        "y": 80
    },
    {
        "start": 26.435,
        "end": 26.676,
        "y": 340
    },
    {
        "start": 26.757,
        "end": 27.083,
        "y": 260
    },
    {
        "start": 27.051,
        "end": 27.377,
        "y": 170
    },
    {
        "start": 27.377,
        "end": 27.738,
        "y": 80
    },
    {
        "start": 27.738,
        "end": 27.951,
        "y": 340
    },
    {
        "start": 28.031,
        "end": 28.358,
        "y": 260
    },
    {
        "start": 28.292,
        "end": 28.781,
        "y": 170
    },
    {
        "start": 28.633,
        "end": 28.965,
        "y": 80
    },
    {
        "start": 28.965,
        "end": 29.211,
        "y": 340
    },
    {
        "start": 29.261,
        "end": 29.707,
        "y": 260
    },
    {
        "start": 29.607,
        "end": 29.853,
        "y": 170
    },
    {
        "start": 29.902,
        "end": 30.229,
        "y": 80
    },
    {
        "start": 30.229,
        "end": 30.481,
        "y": 340
    },
    {
        "start": 30.548,
        "end": 30.93,
        "y": 260
    },
    {
        "start": 30.864,
        "end": 31.461,
        "y": 170
    },
    {
        "start": 31.23,
        "end": 31.509,
        "y": 80
    },
    {
        "start": 31.526,
        "end": 31.678,
        "y": 340
    },
    {
        "start": 31.809,
        "end": 32.217,
        "y": 260
    },
    {
        "start": 32.12,
        "end": 32.35,
        "y": 170
    },
    {
        "start": 32.399,
        "end": 32.749,
        "y": 80
    },
    {
        "start": 32.749,
        "end": 32.9,
        "y": 340
    },
    {
        "start": 33.017,
        "end": 33.316,
        "y": 260
    },
    {
        "start": 33.332,
        "end": 33.682,
        "y": 170
    },
    {
        "start": 33.699,
        "end": 34.026,
        "y": 80
    },
    {
        "start": 34.026,
        "end": 34.24,
        "y": 340
    },
    {
        "start": 34.324,
        "end": 34.688,
        "y": 260
    },
    {
        "start": 34.622,
        "end": 34.951,
        "y": 170
    },
    {
        "start": 34.986,
        "end": 35.301,
        "y": 80
    },
    {
        "start": 35.301,
        "end": 35.533,
        "y": 340
    },
    {
        "start": 35.617,
        "end": 36.115,
        "y": 260
    },
    {
        "start": 35.915,
        "end": 36.361,
        "y": 170
    },
    {
        "start": 36.245,
        "end": 36.56,
        "y": 80
    },
    {
        "start": 36.56,
        "end": 36.794,
        "y": 340
    },
    {
        "start": 36.861,
        "end": 37.225,
        "y": 260
    },
    {
        "start": 37.176,
        "end": 37.459,
        "y": 170
    },
    {
        "start": 37.476,
        "end": 37.81,
        "y": 80
    },
    {
        "start": 37.81,
        "end": 38.09,
        "y": 340
    },
    {
        "start": 38.122,
        "end": 38.456,
        "y": 260
    },
    {
        "start": 38.388,
        "end": 38.606,
        "y": 170
    },
    {
        "start": 38.707,
        "end": 38.907,
        "y": 80
    },
    {
        "start": 39.039,
        "end": 39.173,
        "y": 340
    },
    {
        "start": 39.324,
        "end": 39.501,
        "y": 260
    },
    {
        "start": 39.469,
        "end": 39.599,
        "y": 170
    },
    {
        "start": 39.666,
        "end": 39.829,
        "y": 80
    },
    {
        "start": 39.829,
        "end": 39.929,
        "y": 340
    },
    {
        "start": 39.979,
        "end": 40.192,
        "y": 260
    },
    {
        "start": 40.16,
        "end": 40.29,
        "y": 170
    },
    {
        "start": 40.307,
        "end": 40.49,
        "y": 80
    },
    {
        "start": 40.49,
        "end": 40.603,
        "y": 340
    },
    {
        "start": 40.62,
        "end": 40.783,
        "y": 260
    },
    {
        "start": 40.75,
        "end": 40.884,
        "y": 170
    },
    {
        "start": 40.916,
        "end": 41.094,
        "y": 80
    },
    {
        "start": 41.094,
        "end": 41.226,
        "y": 340
    },
    {
        "start": 41.243,
        "end": 41.456,
        "y": 260
    },
    {
        "start": 41.407,
        "end": 41.57,
        "y": 170
    },
    {
        "start": 41.587,
        "end": 41.75,
        "y": 80
    },
    {
        "start": 41.767,
        "end": 41.883,
        "y": 340
    },
    {
        "start": 41.899,
        "end": 42.095,
        "y": 260
    },
    {
        "start": 42.062,
        "end": 42.209,
        "y": 170
    },
    {
        "start": 42.209,
        "end": 42.37,
        "y": 80
    },
    {
        "start": 42.37,
        "end": 42.5,
        "y": 340
    },
    {
        "start": 42.534,
        "end": 42.736,
        "y": 260
    },
    {
        "start": 42.686,
        "end": 42.852,
        "y": 170
    },
    {
        "start": 42.819,
        "end": 42.985,
        "y": 80
    },
    {
        "start": 43.001,
        "end": 43.149,
        "y": 340
    },
    {
        "start": 43.166,
        "end": 43.282,
        "y": 260
    },
    {
        "start": 43.464,
        "end": 43.626,
        "y": 170
    },
    {
        "start": 43.854,
        "end": 43.952,
        "y": 260
    },
    {
        "start": 44.146,
        "end": 44.276,
        "y": 80
    },
    {
        "start": 44.455,
        "end": 44.603,
        "y": 170
    },
    {
        "start": 44.782,
        "end": 44.931,
        "y": 80
    },
    {
        "start": 45.094,
        "end": 45.242,
        "y": 170
    },
    {
        "start": 45.373,
        "end": 45.503,
        "y": 80
    },
    {
        "start": 45.685,
        "end": 45.852,
        "y": 170
    },
    {
        "start": 46.02,
        "end": 46.202,
        "y": 170
    },
    {
        "start": 46.337,
        "end": 46.455,
        "y": 170
    },
    {
        "start": 46.652,
        "end": 46.785,
        "y": 170
    },
    {
        "start": 46.968,
        "end": 47.097,
        "y": 260
    },
    {
        "start": 47.309,
        "end": 47.474,
        "y": 170
    },
    {
        "start": 47.589,
        "end": 47.704,
        "y": 80
    },
    {
        "start": 47.919,
        "end": 48.082,
        "y": 80
    },
    {
        "start": 48.231,
        "end": 49.324,
        "y": 170
    },
    {
        "start": 49.539,
        "end": 49.688,
        "y": 260
    },
    {
        "start": 49.822,
        "end": 49.971,
        "y": 80
    },
    {
        "start": 50.137,
        "end": 50.271,
        "y": 170
    },
    {
        "start": 50.422,
        "end": 50.554,
        "y": 340
    },
    {
        "start": 50.751,
        "end": 51.134,
        "y": 80
    },
    {
        "start": 51.401,
        "end": 51.763,
        "y": 170
    },
    {
        "start": 52.062,
        "end": 52.214,
        "y": 80
    },
    {
        "start": 52.381,
        "end": 52.683,
        "y": 80
    },
    {
        "start": 52.683,
        "end": 52.851,
        "y": 170
    },
    {
        "start": 52.982,
        "end": 53.148,
        "y": 340
    },
    {
        "start": 53.297,
        "end": 53.747,
        "y": 80
    },
    {
        "start": 53.896,
        "end": 54.278,
        "y": 170
    },
    {
        "start": 54.573,
        "end": 54.723,
        "y": 170
    },
    {
        "start": 54.885,
        "end": 55.037,
        "y": 170
    },
    {
        "start": 55.189,
        "end": 55.351,
        "y": 170
    },
    {
        "start": 55.48,
        "end": 55.659,
        "y": 260
    },
    {
        "start": 55.825,
        "end": 56.037,
        "y": 170
    },
    {
        "start": 56.087,
        "end": 56.286,
        "y": 80
    },
    {
        "start": 56.431,
        "end": 56.613,
        "y": 170
    },
    {
        "start": 56.728,
        "end": 56.909,
        "y": 80
    },
    {
        "start": 57.058,
        "end": 57.224,
        "y": 170
    },
    {
        "start": 57.373,
        "end": 57.585,
        "y": 170
    },
    {
        "start": 57.666,
        "end": 57.913,
        "y": 80
    },
    {
        "start": 57.995,
        "end": 58.222,
        "y": 170
    },
    {
        "start": 58.335,
        "end": 58.5,
        "y": 260
    },
    {
        "start": 58.665,
        "end": 58.828,
        "y": 170
    },
    {
        "start": 58.942,
        "end": 59.167,
        "y": 80
    },
    {
        "start": 59.296,
        "end": 59.443,
        "y": 170
    },
    {
        "start": 59.576,
        "end": 59.724,
        "y": 340
    },
    {
        "start": 59.904,
        "end": 60.117,
        "y": 260
    },
    {
        "start": 60.248,
        "end": 60.428,
        "y": 170
    },
    {
        "start": 60.529,
        "end": 60.676,
        "y": 80
    },
    {
        "start": 60.842,
        "end": 61.237,
        "y": 170
    },
    {
        "start": 61.781,
        "end": 62.847,
        "y": 170
    },
    {
        "start": 63.078,
        "end": 63.16,
        "y": 170
    },
    {
        "start": 63.276,
        "end": 63.408,
        "y": 170
    },
    {
        "start": 63.607,
        "end": 63.719,
        "y": 80
    },
    {
        "start": 63.903,
        "end": 64.053,
        "y": 80
    },
    {
        "start": 64.2,
        "end": 64.347,
        "y": 260
    },
    {
        "start": 64.528,
        "end": 64.678,
        "y": 260
    },
    {
        "start": 64.857,
        "end": 64.975,
        "y": 340
    },
    {
        "start": 65.177,
        "end": 65.328,
        "y": 340
    },
    {
        "start": 65.49,
        "end": 65.656,
        "y": 170
    },
    {
        "start": 65.808,
        "end": 66.668,
        "y": 80
    },
    {
        "start": 66.867,
        "end": 67.518,
        "y": 340
    },
    {
        "start": 68.102,
        "end": 68.184,
        "y": 170
    },
    {
        "start": 68.3,
        "end": 68.502,
        "y": 170
    },
    {
        "start": 68.665,
        "end": 68.815,
        "y": 80
    },
    {
        "start": 68.997,
        "end": 69.181,
        "y": 80
    },
    {
        "start": 69.28,
        "end": 69.429,
        "y": 170
    },
    {
        "start": 69.596,
        "end": 69.763,
        "y": 170
    },
    {
        "start": 69.879,
        "end": 70.223,
        "y": 260
    },
    {
        "start": 70.642,
        "end": 70.791,
        "y": 170
    },
    {
        "start": 70.993,
        "end": 71.207,
        "y": 170
    },
    {
        "start": 71.273,
        "end": 71.357,
        "y": 80
    },
    {
        "start": 71.47,
        "end": 71.634,
        "y": 80
    },
    {
        "start": 71.8,
        "end": 71.935,
        "y": 170
    },
    {
        "start": 72.12,
        "end": 72.316,
        "y": 170
    },
    {
        "start": 72.446,
        "end": 72.744,
        "y": 80
    },
    {
        "start": 73.194,
        "end": 73.295,
        "y": 260
    },
    {
        "start": 73.377,
        "end": 73.541,
        "y": 260
    },
    {
        "start": 73.736,
        "end": 73.835,
        "y": 170
    },
    {
        "start": 73.948,
        "end": 74.098,
        "y": 170
    },
    {
        "start": 74.297,
        "end": 74.395,
        "y": 80
    },
    {
        "start": 74.639,
        "end": 74.881,
        "y": 80
    },
    {
        "start": 74.965,
        "end": 75.308,
        "y": 170
    },
    {
        "start": 75.714,
        "end": 75.782,
        "y": 80
    },
    {
        "start": 75.865,
        "end": 76.538,
        "y": 80
    },
    {
        "start": 77.526,
        "end": 77.671,
        "y": 80
    },
    {
        "start": 77.884,
        "end": 78.031,
        "y": 80
    },
    {
        "start": 78.18,
        "end": 78.623,
        "y": 80
    },
    {
        "start": 78.72,
        "end": 78.788,
        "y": 170
    },
    {
        "start": 78.888,
        "end": 79.038,
        "y": 170
    },
    {
        "start": 80.046,
        "end": 80.164,
        "y": 80
    },
    {
        "start": 80.393,
        "end": 80.59,
        "y": 80
    },
    {
        "start": 80.607,
        "end": 80.773,
        "y": 170
    },
    {
        "start": 80.905,
        "end": 81.305,
        "y": 80
    },
    {
        "start": 81.657,
        "end": 81.872,
        "y": 170
    },
    {
        "start": 81.985,
        "end": 82.149,
        "y": 80
    },
    {
        "start": 82.166,
        "end": 82.429,
        "y": 170
    },
    {
        "start": 82.511,
        "end": 82.729,
        "y": 80
    },
    {
        "start": 82.811,
        "end": 83.277,
        "y": 170
    },
    {
        "start": 83.392,
        "end": 83.458,
        "y": 80
    },
    {
        "start": 83.56,
        "end": 83.775,
        "y": 80
    },
    {
        "start": 83.792,
        "end": 84.058,
        "y": 170
    },
    {
        "start": 84.09,
        "end": 84.392,
        "y": 80
    },
    {
        "start": 84.425,
        "end": 84.659,
        "y": 170
    },
    {
        "start": 84.707,
        "end": 84.957,
        "y": 260
    },
    {
        "start": 85.041,
        "end": 85.42,
        "y": 170
    },
    {
        "start": 85.437,
        "end": 85.604,
        "y": 80
    },
    {
        "start": 85.67,
        "end": 85.964,
        "y": 170
    },
    {
        "start": 85.998,
        "end": 86.525,
        "y": 80
    },
    {
        "start": 87.072,
        "end": 87.173,
        "y": 260
    },
    {
        "start": 87.256,
        "end": 87.469,
        "y": 260
    },
    {
        "start": 87.6,
        "end": 87.815,
        "y": 170
    },
    {
        "start": 87.881,
        "end": 88.395,
        "y": 80
    },
    {
        "start": 88.629,
        "end": 89.089,
        "y": 260
    },
    {
        "start": 89.105,
        "end": 89.677,
        "y": 170
    },
    {
        "start": 89.761,
        "end": 90.794,
        "y": 80
    },
    {
        "start": 91.122,
        "end": 93.143,
        "y": 170
    },
    {
        "start": 93.704,
        "end": 95.659,
        "y": 80
    }
]

# --- Auto-load generated platform data if available ---
import json as _json, os as _os
_gen = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'platforms_generated.json')
if _os.path.exists(_gen):
    with open(_gen) as _f:
        PLATFORM_DATA = _json.load(_f)
# --- End auto-load ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

PLAYER_W = 50
PLAYER_H = 50

player_frames = []
for f in ["frame1.png", "frame2.png", "frame3.png", "jump.png"]:
    img = pygame.image.load(os.path.join(ASSETS_DIR, f)).convert_alpha()
    player_frames.append(pygame.transform.scale(img, (PLAYER_W, PLAYER_H)))

if music_available:
    try:
        pygame.mixer.music.load(os.path.join(ASSETS_DIR, "wait for you.mp3"))
    except pygame.error:
        music_available = False

# -------------------
# Constants
# -------------------
SCROLL_SPEED      = 12
PLAYER_X          = 150
PLATFORM_H        = 40
FALL_SPEED        = 14
MAX_ARC           = 170       # max pixel overshoot on a full-length jump
STEP_THRESHOLD    = 0.25      # seconds: gap <= this => smooth step, no arc
INTRO_WALK_DUR    = 3.0       # seconds of walking before music starts
DATA_Y_GROUND     = 340       # lowest data-y
SCREEN_GROUND     = 450       # where data_y=340 maps on screen

font_ui    = pygame.font.SysFont(None, 46)
font_small = pygame.font.SysFont(None, 30)

# -------------------
# Helper: coordinate mapping
# -------------------
def dsy(data_y):
    """Convert platform data-y to screen-y."""
    return data_y + (SCREEN_GROUND - DATA_Y_GROUND)

# -------------------
# Build sorted platform sequence
# -------------------
PLATFORMS = sorted(PLATFORM_DATA, key=lambda p: p['start'])

# -------------------
# Helper functions
# -------------------
def clamp01(v):
    return max(0.0, min(1.0, v))

def ease_inout(t):
    return t * t * (3.0 - 2.0 * t)

def find_next(current_idx):
    """Return (idx, platform) immediately after current_idx."""
    nxt = current_idx + 1
    if nxt < len(PLATFORMS):
        return nxt, PLATFORMS[nxt]
    return None, None

def compute_fly_y(t, t0, t1, y0, y1, do_arc):
    """Interpolate character screen-y during a flight segment."""
    if t1 <= t0:
        return y1
    p = clamp01((t - t0) / (t1 - t0))
    if do_arc:
        base = y0 + (y1 - y0) * p
        duration = t1 - t0
        arc_h = clamp01(duration / 0.8) * MAX_ARC
        arc_h = max(arc_h, 40)
        return base - arc_h * math.sin(math.pi * p)
    else:
        return y0 + (y1 - y0) * ease_inout(p)

# -------------------
# Game states
# -------------------
S_IDLE    = "IDLE"       # waiting at start
S_WALK    = "WALKING"    # held space, intro walk
S_FLY     = "AIRBORNE"   # jump or smooth step
S_RUN     = "ON_PLATFORM"
S_FALL    = "FALLING"

# -------------------
# State variables
# -------------------
state          = S_IDLE
music_started  = False
music_time     = -INTRO_WALK_DUR   # negative = pre-music, 0+ = in song

first_plat_y   = dsy(PLATFORMS[0]['y'])
cur_plat_idx   = -1                # -1 = on intro platform
cur_plat_y     = first_plat_y      # screen-y of top of current platform

fly_t0 = fly_t1 = 0.0
fly_y0 = fly_y1 = 0.0
fly_arc = False

player_rect = pygame.Rect(PLAYER_X, int(cur_plat_y) - PLAYER_H, PLAYER_W, PLAYER_H)

# -------------------
# Main Loop
# -------------------
running = True
while running:
    dt = clock.tick(60) / 1000.0

    # --- advance music time ---
    if music_started:
        if music_available:
            music_time = pygame.mixer.music.get_pos() / 1000.0
        else:
            music_time += dt
    elif state == S_WALK:
        music_time += dt  # walks from -INTRO_WALK_DUR toward 0

    screen.fill((20, 20, 35))

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state == S_IDLE:
                state      = S_WALK
                music_time = -INTRO_WALK_DUR

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:

            if state == S_WALK:
                # --- tutorial jump: release space -> start music, fly to first platform ---
                music_started = True
                music_time    = 0.0
                if music_available:
                    pygame.mixer.music.play()

                p0      = PLATFORMS[0]
                fly_t0  = 0.0
                fly_t1  = p0['start']
                fly_y0  = cur_plat_y
                fly_y1  = dsy(p0['y'])
                gap     = fly_t1 - fly_t0
                fly_arc = gap >= STEP_THRESHOLD

                cur_plat_idx = 0
                state        = S_FLY

            elif state == S_RUN:
                # --- find next platform and decide jump vs step ---
                next_idx, next_p = find_next(cur_plat_idx)
                if next_p is not None:
                    t_now  = music_time
                    t_land = next_p['start']
                    gap    = max(0.0, t_land - t_now)

                    fly_t0  = t_now
                    fly_t1  = t_now + gap
                    fly_y0  = cur_plat_y
                    fly_y1  = dsy(next_p['y'])
                    fly_arc = gap >= STEP_THRESHOLD

                    cur_plat_idx = next_idx
                    state        = S_FLY
                else:
                    state = S_FALL

    # --- state machine update ---
    if state == S_FLY:
        if music_time >= fly_t1:
            # landed
            cur_plat_y    = fly_y1
            player_rect.y = int(cur_plat_y) - PLAYER_H

            p = PLATFORMS[cur_plat_idx]
            if music_time <= p['end'] + 0.1:
                state = S_RUN
            else:
                state = S_FALL
        else:
            char_y        = compute_fly_y(music_time, fly_t0, fly_t1,
                                          fly_y0, fly_y1, fly_arc)
            player_rect.y = int(char_y) - PLAYER_H

    elif state == S_RUN:
        player_rect.y = int(cur_plat_y) - PLAYER_H
        p = PLATFORMS[cur_plat_idx]
        if music_time > p['end'] + 0.08:
            state = S_FALL

    elif state in (S_IDLE, S_WALK):
        player_rect.y = int(cur_plat_y) - PLAYER_H

    elif state == S_FALL:
        player_rect.y += int(FALL_SPEED)
        if player_rect.top > HEIGHT:
            if music_started and music_available:
                pygame.mixer.music.stop()
            music_started  = False
            music_time     = -INTRO_WALK_DUR
            state          = S_IDLE
            cur_plat_idx   = -1
            cur_plat_y     = first_plat_y
            player_rect.y  = int(cur_plat_y) - PLAYER_H

    # --- draw intro platform ---
    # extends from 5 sec before first platform up to its start
    intro_end   = PLATFORMS[0]['start']
    intro_start = intro_end - 5.0
    ix = (intro_start * 60 * SCROLL_SPEED) - (music_time * 60 * SCROLL_SPEED) + PLAYER_X
    iw = (intro_end - intro_start) * 60 * SCROLL_SPEED
    isy = first_plat_y
    if ix + iw > 0:
        pygame.draw.rect(screen, (55, 55, 90), (int(ix), int(isy), int(iw), PLATFORM_H))

    # --- draw beat platforms (multi-height) ---
    for p in PLATFORMS:
        xp = (p['start'] * 60 * SCROLL_SPEED) - (music_time * 60 * SCROLL_SPEED) + PLAYER_X
        wp = (p['end'] - p['start']) * 60 * SCROLL_SPEED
        sy = dsy(p['y'])
        if -wp < xp < WIDTH:
            col = (120, 120, 255)
            pygame.draw.rect(screen, col, (int(xp), int(sy), int(wp), PLATFORM_H))

    # --- draw player ---
    run_frame = int(pygame.time.get_ticks() / 100) % 3
    if state == S_FLY and fly_arc:
        frame = 3
    elif state == S_FALL:
        frame = 3
    elif state == S_IDLE:
        frame = 0
    else:
        frame = run_frame
    screen.blit(player_frames[frame], (player_rect.x, player_rect.y))

    # --- UI instructions ---
    if state == S_IDLE:
        txt = font_ui.render("Hold [SPACE] to start walking", True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    elif state == S_WALK:
        txt = font_ui.render("Release [SPACE] to jump!", True, (255, 215, 60))
        screen.blit(txt, txt.get_rect(center=(WIDTH // 2, 70)))
        hint = font_small.render("Land on the first platform to begin", True, (180, 180, 220))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 110)))

    pygame.display.update()

pygame.quit()
