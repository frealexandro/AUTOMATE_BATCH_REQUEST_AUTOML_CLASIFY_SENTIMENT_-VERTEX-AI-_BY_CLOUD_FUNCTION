from params import *
from input_data import *
from data_frame import *
from generator import *
from generator_path import *
import pandas as pd
import numpy as np
from google.cloud import aiplatform

# from google.cloud.aiplatform.gapic.schema import predict
# from google.protobuf import json_format
# from google.protobuf.struct_pb2 import Value
from typing import Sequence, Union
import gcsfs


def batch_prediction_job(
    project: str,
    location: str,
    model_resource_name: str,
    job_display_name: str,
    gcs_source: Union[str, Sequence[str]],
    gcs_destination: str,
    sync: bool = True,
):

    aiplatform.init(project=project, location=location)

    my_model = aiplatform.Model(model_resource_name)

    batch_prediction_job = my_model.batch_predict(
        job_display_name=job_display_name,
        gcs_source=gcs_source,
        gcs_destination_prefix=gcs_destination,
        sync=sync,
    )


def run(event, context):

    # Call Params to find read data
    Params = Param()
    filename = event["name"]
    input_bucket = event["bucket"]

    Route_m = "gs://{0}/{1}".format(input_bucket, filename)
    print(f"The Params is: Ok")

    # Extract the Data
    All_Data = Input_Data(Route_m)
    Data = All_Data.Data_Sent()
    print(f"The Data is: Ok")

    # Extract the Sentiment
    Extract = Data_Frame(Data)
    Data_Sentiment = Extract.Transform()
    print(f"The sentiment export to list is: Ok")

    # Generate Data files txt
    Variable_S = Generator(Data_Sentiment, Params.Processing_Batch)
    Sentiments = Variable_S.Iterator()
    print(f"The sentiment already exported to txt : Ok ")

    # Generate list with paths of sentiments
    list_sent = Generate_path(Data_Sentiment, Params.Path_Control)
    jsonl = list_sent.paths_jsl(Params.complement_ini, Params.complement_end)
    print("The Paths  prediction exported : OK ")

    # Batch prediction
    print("Prediction Batch: ok")
    batch_prediction_job(
        Params.project_id,
        Params.location,
        # change depend of the model offsite - onsite
        Params.model_id_off_site,
        Params.job_display_name,
        Params.input_uri,
        Params.output_uri,
    )
