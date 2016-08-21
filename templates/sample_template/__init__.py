__all__=['SampleTemplate']

from template_base import TemplateBase

class SampleTemplate(TemplateBase):
    def __init__(self):
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
        return path.join(dirname(__file__), 'template.tex')
