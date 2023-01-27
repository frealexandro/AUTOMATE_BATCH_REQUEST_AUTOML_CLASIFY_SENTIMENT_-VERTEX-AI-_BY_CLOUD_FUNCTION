# cloud function batch python 

_In this project, we create a cloud function in GCP using the FLASK framework that is triggered by a bucket and executes a batch prediction of a sentiment analysis model._

## Starting 🚀

_To get the project on your local machine, please clone the repository named cloud_function_python. Note that you must have permission from the organization to do so._

### Pre requirements 📋

_This project must be run directly in a GCP cloud function with Python 3.10 language or if desired it can also be run directly in your virtual machine with some modifications. You must install the following dependencies in the cloud function or virtual environment, as listed in the file requirements.txt:_

```
pip install -r requeriments.txt
```
_In the cloud function, it is only necessary to load the file, and once it is done, DEPLOY it. The dependencies will be installed automatically._


###installation 🔧


1.A cloud function must be created in GCP with a bucket trigger to make the batch. We will modify different paths where we will perform **processing, input, and output** of the data. We also need to modify our **project id, model id, location, job_name**. Note that this project creates a jsonl file as the model for **sentiment analysis** was built in this way. To understand more about how to make a batch prediction, see the links in this readme. To modify these parameters, see the file **params.py**


```
'self.project_id = "284757810904"'

'self.model_id_off_site ="5835259941211865088"'

'self.input_uri = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Main_Control_Batch/Prediction_Main_Batch.jsonl"'

'self.output_uri = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/"'

'self.location="us-central1"'

'self.job_display_name = "new_job"'

'self.Processing_Batch = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/"'
 
 'self.Path_Control = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Main_Control_Batch/"'
 
 'self.complement_ini = "{\'content\' :\'gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/"'
 
  'self.complement_end = ".txt\', \'mimeType\': \'text/plain\'}"'


```

## running the tests ⚙️


_The cloud function is at its maximum performance, this batch is to make a batch more or less 7000 records. In the event that it is more gigantic in the future, a more scalable solution must be implemented with another Google Cloud service, but we are referring to perhaps more than 50 GB of processing. For now, the cloud function, being designed with OOP, is relatively very stable and scalable._

###Analyze end-to-end tests🔩


_If the whole process is executed correctly, the cloud function response will show the message "JobState.JOB_STATE_SUCCEEDED" on GCP logs. Before this message appears, the following messages should be displayed:_

```
The Params is: Ok
The Data is: Ok
The sentiment export to list is: Ok
The sentiment already exported to txt : Ok
The Paths  prediction exported : OK 
Prediction Batch: ok

```

### coding style ⌨️

_This program was completely modularized through object-oriented programming and also attempted to be codified under the PEP 8 regime._



## Built by 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Parameterization Guide
* [PANDAS](https://pandas.pydata.org/) - data handling library
* [FLASK](https://flask.palletsprojects.com/en/2.2.x/) - Freamwork API
* [CLOUD FUNCTIONS](https://cloud.google.com/functions/docs/concepts/overview) - Cloud Functions overview
* [BATCH PREDICTIONS](https://cloud.google.com/vertex-ai/docs/predictions/overview#batch_predictions) - Overview of getting predictions on Vertex AI
* [Vertex AI](https://cloud.google.com/vertex-ai/docs/training/create-training-pipeline) - Create training pipelines

## Versioning 📌

For all available versions, see the [tags en este repositorio](https://github.com/frealexandro/cloud_function_batch_python).

## Authors ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)

