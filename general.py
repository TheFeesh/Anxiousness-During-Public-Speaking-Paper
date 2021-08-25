import pandas as pd
from sklearn.model_selection import train_test_split

path_to_features = (
    r"C:\Users\Sean\Downloads\VerBIO-20210706T165918Z-001\VerBIO\TEST01\Features\IS10.xlsx")
path_to_survey_scores = (
    r"C:\Users\Sean\Downloads\VerBIO\TEST01\Self_Reports\TEST01_afterPPT.xlsx")

Surveydf = pd.read_excel(path_to_survey_scores, engine='openpyxl')
Featuresdf = pd.read_excel(path_to_features, engine='openpyxl')

# features and targets (X and y)
# prepare data
prediction_target = Surveydf['State Anxiety Enthusiasm Score']
data = Featuresdf[list(Featuresdf)]
del data['PID']

train_data, validation_data, train_target, validation_target = train_test_split(
    data, prediction_target, random_state=1)


def find_pid_row(path, pid):
    # given a pid, find what row the pid is in

    df = pd.read_excel(path, engine='openpyxl')
    row = df.loc[df['PID'] == pid].index[0]

    return row


def get_participant_features(path, pid):
    # gets the row given the pid
    df = pd.read_excel(path, engine='openpyxl')
    features = df.loc[find_pid_row(path, pid)]
    return features


def get_survey_score(path, pid, row):
    # gets specific survey score of a participant given pid and row #
    df = pd.read_excel(path, engine='openpyxl')
    score = df['State Anxiety Enthusiasm Score'].loc[row]
    return score
