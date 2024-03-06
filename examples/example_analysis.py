# pip3 install '/Users/willkemp/Python/GitHub/appaa'

from appaa.postanalysis import Analysis
from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data

df = load_data()

estimator = DifferenceInMeans(alpha=0.05, beta=0.8)
analyse = Analysis(data=df, test_ids=[1], control_ids=[0], estimator=estimator)
output = analyse.results()
print(output.head())