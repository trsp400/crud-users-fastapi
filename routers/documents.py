from fastapi import APIRouter, File, UploadFile
from io import BytesIO
import pandas as pd

router = APIRouter()

@router.post('/upload')
def read_csv(file: UploadFile = File(...)):
  contents = file.file.read()
  buffer = BytesIO(contents)
  df = pd.read_csv(buffer)
  buffer.close()
  
  print(df)
  
  file.file.close()
  # return df.to_dict()