from fast_bert.prediction import BertClassificationPredictor


modelFRPath = 'FR/model/'
labelFRPath = 'FR/'

modelENPath = 'EN/model/'
labelENPath = 'EN/'

"""
#En local
modelFRPath = 'app/FR/model/'
labelFRPath = 'app/FR/'

modelENPath = 'app/EN/model/'
labelENPath = 'app/EN/'
"""

predictorFR = BertClassificationPredictor(
    label_path=labelFRPath,
    model_path=modelFRPath,
    multi_label=True,
    model_type='camembert-base',
    do_lower_case=False)

predictorEN = BertClassificationPredictor(
    label_path=labelENPath,
    model_path=modelENPath,
    multi_label=True,
    model_type='bert',
    do_lower_case=False)


