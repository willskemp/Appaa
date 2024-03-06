from appaa.analysis import Analysis
from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data
import numpy as np

test_df = load_data()
test_estimator = DifferenceInMeans()
test_postanalysis = Analysis(
    data=test_df, test_ids=[1], control_ids=[0], estimator=test_estimator
)


def test_obs_to_array(postanalysis: Analysis = test_postanalysis):
    test_obs = postanalysis._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray