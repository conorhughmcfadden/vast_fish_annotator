from navigate.tools.decorators import FeatureList
from navigate.model.features.feature_related_functions import (
    VastFishAnnotator,
)


@FeatureList
def vast_fish_annotator():
    return [
        {"name": VastFishAnnotator},
    ]
