# import needed libraries
import csv
import datasets
from arabert.preprocess import ArabertPreprocessor

# load arabert to preprocess the data
model_name="bert-base-arabert"
arabert_prep = ArabertPreprocessor(model_name=model_name, keep_emojis=False)

_DESCRIPTION = """\
The Arabic Empathetic DataSet contains ~43K samples of open domain conversation with 3 previous history utterances, the emotion of the context, and empathetic responses.
"emotion" refers to the emotion in the context
"context" refers to the 3 previous history utterances from the conversation
"response" refers to the empathetic response
"""

# build our dataset classes
class ArabicEmpConvDataset(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="arabic_emp_3_history_conv",
            version=datasets.Version("1.0.0"),
            description="Full training set",
        ),
    ]

    # define datasets information and its features
    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "emotion": datasets.Value("string"),
                    "context": datasets.Value("string"),
                    "response": datasets.Value("string")
                }
            ),
            supervised_keys=None,
        )

    # define the split of our data here its Train and Test
    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"filepath": './Dataset/processed/train_arabic_with_history.csv'},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": './Dataset/processed/test_arabic_history.csv'},
            )
        ]

    # load the data
    def _generate_examples(self, filepath):
        with open(filepath,'r',encoding='utf-8') as f:
        # with open("./Dataset/processed/train_arabic_with_history.csv",'r',encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for i , row in enumerate(csv_reader):
                if i==0:
                    continue
                yield i-1, {
                    "emotion": arabert_prep.preprocess(row[0]),
                    "context": arabert_prep.preprocess(row[1]),
                    "response": row[2]
                }