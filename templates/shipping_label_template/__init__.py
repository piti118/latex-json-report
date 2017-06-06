import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from template_base import TemplateBase
from os import path
import shutil


__all__ = ['template']


def template():
    return ShippingLabelTemplate()


class ShippingLabelTemplate(TemplateBase):

    def __init__(self):
        super().__init__(path.dirname(__file__))  # this setup jinja loader
        pass

    def preprocess(self, data, cwd):
        """
        should return a dictionary with all the data
        some additional data might be build here
        This is the place where we should render graph and put the output
        file name in the directory
        """

        asset_dir = path.join(path.dirname(__file__), 'assets')
        shutil.copytree(asset_dir, path.join(cwd, 'assets'))  # should we symlink instead?
        return data

    def get_template(self, data):
        return 'template.tex'

    def sample_data(self):
        return {"name": 'พี่เสือ โทนี่'}
