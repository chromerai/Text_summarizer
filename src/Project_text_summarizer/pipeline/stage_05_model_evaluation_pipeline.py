from Project_text_summarizer.config.configuration import ConfigurationManager
from Project_text_summarizer.components.model_evaluation import ModelEvaluation
from Project_text_summarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()