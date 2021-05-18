from questeval.questeval_metric import QuestEval

from tests.resources.constants import (
    SRC_1, HYP_1, RES_1
)

def test_questeval_metric():
    questeval = QuestEval()
    score = questeval.compute_all(HYP_1, SRC_1)
    assert score == RES_1
