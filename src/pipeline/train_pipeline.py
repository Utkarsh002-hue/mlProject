from src.components.dataingestion import DataIngestion
from src.components.datatransform import DataTransformation
from src.components.modelTrainer import ModelTrainer

if __name__ == "__main__": 
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)

# 