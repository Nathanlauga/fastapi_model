from typing import List

import joblib
import numpy as np
from loguru import logger

from app.utils import utils
from app.core.messages import NO_VALID_PAYLOAD
from app.models.payload import (Data, payload_to_list)
from app.models.prediction import PredictionResult


class Model(object):

    def __init__(self, path):
        self.path = path
        self._load_local_model()

    def _load_local_model(self):
        self.model = joblib.load(self.path)

    def _pre_process(self, payload: Data) -> List:
        logger.debug("Pre-processing payload.")
        
        logger.debug(payload)
        
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> PredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()[0]

        # custom attributes you can add
        details = utils.prediction_class_str(result)

        pred = PredictionResult(prediction=result, details=details)
        return pred

    def _predict(self, features: List) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload: Data):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result