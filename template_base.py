from latex_jinja import latex_jinja
import latex_compiler
from os import path

__all__ = ['TemplateBase']


class TemplateBase:
    def __init__(self, template_path):
        self.jinja = latex_jinja(template_path)
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
        return None

    def compile(self, data, cwd):
        # evaluate template
        data = self.preprocess(data, cwd)
        print(data)
        template_file = self.get_template(data)
        if template_file is None:
            raise Exception('template_file returns None: Did you override get_template?')
        print(template_file, 'sssss')
        template = self.jinja.get_template(template_file)
        print(template, 'wwwww')
        output = template.render(**data)
        print(output)
        # write output to file ready to compile
        driver_file = path.join(cwd, 'driver.tex')
        with open(driver_file, 'w') as f:
            f.write(output)

        # compile
        pdf_file = latex_compiler.compile(driver_file, cwd)
        print(pdf_file)
        return pdf_file
