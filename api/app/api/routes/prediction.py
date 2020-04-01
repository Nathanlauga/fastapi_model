from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.core import security
from app.models.payload import Data
from app.models.prediction import PredictionResult
from app.services.model import Model

router = APIRouter()


@router.post("/predict", response_model=PredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: Data = None
) -> PredictionResult:

    model: Model = request.app.state.model
    prediction: PredictionResult = model.predict(block_data)

    return prediction