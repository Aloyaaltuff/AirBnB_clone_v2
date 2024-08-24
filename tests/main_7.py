#!/usr/bin/env python3
from models.base_model import BaseModel
from models import storage

# Create and save an instance
bm1 = BaseModel()
bm1.save()

# Reload and verify the objects
storage.reload()
bm2 = list(storage.all().values())[0]
print(bm1.to_dict() == bm2.to_dict())  # Should print True

