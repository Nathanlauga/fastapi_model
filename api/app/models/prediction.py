from pydantic import BaseModel


class PredictionResult(BaseModel):
    """Class for prediction result

    This will be the return of predict endpoint
    """
    prediction: int
    details: str