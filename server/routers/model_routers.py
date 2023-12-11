from fastapi import APIRouter, UploadFile, HTTPException
from schemes import *
from ai import *

model_api = APIRouter(prefix='/api/model', tags=['model'])


@model_api.post('', response_model=ModelBaseSchema)
async def upload(text):
    answer = predict(text)
    response = {'target_name': answer[0][0], 'probability': answer[1][0]}

    return response
