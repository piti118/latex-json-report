from template_base import TemplateBase
from os import path

__all__ = ['template']


def template():
    return BasicTemplate()


class BasicTemplate(TemplateBase):
    def __init__(self):
        super().__init__(path.dirname(__file__)) #this setup jinja loader
        pass

    def preprocess(self, data, cwd):
        """
        should return a dictionary with all the data
        some additional data might be build here
        This is the place where we should render graph and put the output
        file name in the directory
        """
        return data

    def get_template(self, data):
        return 'template.tex'

    def sample_data(self):
        return {"x": 2, "y": "hellooooooooooow"}
