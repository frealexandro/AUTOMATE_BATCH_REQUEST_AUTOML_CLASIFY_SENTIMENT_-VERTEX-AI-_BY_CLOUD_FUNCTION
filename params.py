  #"""This part we will found  all parameters that use on this program"""

class Param:
    
    def __init__(self):
         
        #Path Bucket
        #self.file_input = 'gs://data_sentiment_v5/SSS/sss_offsite/off_site_2022/off_site_last.xlsx'

        #Params Request
        self.project_id = "284757810904"
        #8083737030757974016
        
        #change depend of the origin file
        self.model_id_off_site ="5835259941211865088"
        
        
        
        self.input_uri = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Main_Control_Batch/Prediction_Main_Batch.jsonl"
         
        self.output_uri = "gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/"
        
        self.location="us-central1"
        
        self.job_display_name = "new_job"
        
        #Params masive data
        
        self.Processing_Batch = 'gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/'
        
        self.Path_Control = 'gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Main_Control_Batch/'
        
        self.complement_ini = "{\'content\' :\'gs://batch_predictions_sentiment/Prediction_Masive_Sentiment/Prosecing_Masive_Data/"
        
        self.complement_end = ".txt\', \'mimeType\': \'text/plain\'}"