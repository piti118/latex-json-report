from latex_jinja import latex_jinja
from latex_compiler import latex_compiler

__all__ = ['TemplateBase']


class TemplateBase:
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
        return None

    def compile(self, data, cwd):
        # evaluate template
        template_file = self.get_template()
        if template_file is None:
            raise Exception('template_file returns None: Did you override get_template?')
        template = latex_jinja.get_template(template_file)
        output = template.render(**data)

        # write output to file ready to compile
        driver_file = path.join(cwd, 'driver.tex')
        with open(driver_file, 'w') as f:
            f.write(output)

        # compile
        return latex_compiler.compile(driver_file, tempdir)
