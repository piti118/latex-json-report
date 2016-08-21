from templates import sample_template
from os import path

tmpdir = path.join(path.dirname(__file__), 'temp')

t = sample_template.SampleTemplate()
t.compile({"x": "abc", "y": "def"}, tmpdir)
