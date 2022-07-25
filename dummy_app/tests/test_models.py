import os
from django.test import TestCase
import pandas as pd

from dummy_app.models import Setai, Setaiin


class ModelTest(TestCase):

    def setUp(self) -> None:
        setai_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '世帯.csv'))
        for _, row in setai_df.iterrows():
            data = row.to_dict()
            print(data)
            Setai.objects.create(**data)

        setaiin_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '世帯員.csv'))
        for _, row in setaiin_df.iterrows():
            data = row.to_dict()
            Setaiin.objects.create(**data)

    def test_models(self):
        self.assertEqual(Setai.objects.all().count(), 3)
        self.assertEqual(Setaiin.objects.all().count(), 6)
        takahashi = Setai.objects.filter(sei='高橋').prefetch_related('setaiin_set')
        self.assertEqual(takahashi[0].id, 3)
        self.assertEqual(takahashi[0].setaiin_set.all().count(), 2)


