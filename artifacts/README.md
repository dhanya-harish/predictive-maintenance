---
tags:
- sklearn
- predictive-maintenance
- classification
- automotive
library_name: sklearn
license: apache-2.0
pipeline_tag: text-classification
---

# Engine Predictive Maintenance Model

**Best model:** `GradientBoosting`  
**F1 (test):** 0.7657

## Usage

```python
import pickle, pandas as pd
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)
# X = pd.DataFrame([{
#     'engine_rpm': 2500, 'lub_oil_pressure': 4.2, 'fuel_pressure': 110,
#     'coolant_pressure': 1.2, 'lub_oil_temp': 95, 'coolant_temp': 88
# }])
# pred = model.predict(X)[0]
```

## Notes
- Tuned via GridSearchCV (scoring=F1), metrics logged with MLflow.