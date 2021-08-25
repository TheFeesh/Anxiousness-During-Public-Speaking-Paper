import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

from general import *
# open and read excel files

# model w/o splitting
decision_tree_model = DecisionTreeRegressor(random_state=1)
decision_tree_model.fit(data, prediction_target)
nosplitpredictions = decision_tree_model.predict(data)
#print(mean_absolute_error(prediction_target, nosplitpredictions))

# model
decision_tree_model = DecisionTreeRegressor()
decision_tree_model.fit(train_data, train_target)

# predicion
predictions = decision_tree_model.predict(validation_data)
print(f"{100-((mean_absolute_error(validation_target, predictions)/prediction_target.mean())*100)}% Accurate")
