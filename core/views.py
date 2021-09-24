from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        '''Retorna 12 labels para a presentação do x'''
        labels = [
            "Janeiro",
            "Fevereiro",
            "Marco",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    def get_providers(self):
        '''Retorna o s nomes dos datasets.'''

        datasets = [
            "Programação em Python",
            "Banco de Dados",
            "Django Essencial",
            "Git e GitHub",
            "HTML",
            "CSS",
            "Javascript",
        ]
        return datasets

    def get_data(self):
        """

        :return: Retorna 7 datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        7 datasets, então 7 linhas.
        """

        dados = []
        for linhas in range(7):
            for colunas in range(12):
                dado = [
                    randint(1, 10),  # jan
                    randint(1, 10),  # fev
                    randint(1, 10),  # mar
                    randint(1, 10),  # abr
                    randint(1, 10),  # mai
                    randint(1, 10),  # jun
                    randint(1, 10),  # jul
                    randint(1, 10),  # ago
                    randint(1, 10),  # set
                    randint(1, 10),  # out
                    randint(1, 10),  # nov
                    randint(1, 10)   # dez
                ]
            dados.append(dado)
        return dados
