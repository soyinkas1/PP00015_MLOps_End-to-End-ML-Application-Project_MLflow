from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger
from pathlib import Path


STAGE_NAME = 'Model Evaluation Stage'


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x')
    except Exception as e:
        logger.exception(e)
        raise e

