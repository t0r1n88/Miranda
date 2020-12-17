import os
from pathlib import Path
PATH_TO_FIlES = '../data/'

# path = Path(PATH_TO_FIlES)
#
# for file in path.glob('*.xlsx'):
#     print(file)

for file in os.listdir(PATH_TO_FIlES):
    print(file)