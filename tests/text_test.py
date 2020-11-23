# -*- coding: UTF-8 -*-

# Import from standard library
import os
import clem_useful_functions
import pandas as pd
# Import from our lib
from clem_useful_functions.lib import clean_data
import pytest



def test_preprocess_text():
    assert preprocess_text("In those days cheap apartments were almost impossible to find in Manhattan, so I had to move to Brooklyn. 966") === 'days cheap apartments almost impossible find manhattan move brooklyn'
