#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.base_model import BaseModel

# Create an instance and call reload
bm = BaseModel()
bm.save()
from models import storage
print(type(storage.reload()))

