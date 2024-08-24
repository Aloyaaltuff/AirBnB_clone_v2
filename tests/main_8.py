#!/usr/bin/env python3
from models.base_model import BaseModel
from models import storage

# Create instance and save
bm1 = BaseModel()
bm1.save()

# Reload and check equality
storage.reload()
bm2 = list(storage.all().values())[0]

# Check if the reloaded object matches the saved object
print(bm1.to_dict())
print(bm2.to_dict())
print(bm1.to_dict() == bm2.to_dict())  # Should print True

