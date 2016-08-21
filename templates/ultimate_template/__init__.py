import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from template_base import TemplateBase
from os import path
import shutil


__all__ = ['template']

def template():
    return UltimateTemplate()

class UltimateTemplate(TemplateBase):
    def __init__(self):
        super().__init__(path.dirname(__file__)) #this setup jinja loader
        pass

    def make_graph(self, data, cwd):
        plt.figure()
        plt.plot(data['raw_numbers'])
        plt.grid(True)
        output = path.join(cwd, 'graph.pdf')
        plt.savefig(output, bbox_inches='tight')


    def preprocess(self, data, cwd):
        """
        should return a dictionary with all the data
        some additional data might be build here
        This is the place where we should render graph and put the output
        file name in the directory
        """
        asset_dir = path.join(path.dirname(__file__), 'assets')
        shutil.copytree(asset_dir, path.join(cwd, 'assets')) #should we symlink instead?
        self.make_graph(data, cwd)
        return data

    def get_template(self, data):
        return 'template.tex'

    def sample_data(self):
        return { "name": "ปิติ", "raw_numbers":[2,4,-3,7] }
