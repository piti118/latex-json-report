FROM python:3.5

RUN apt-get update
RUN apt-get install -y --no-install-recommends texlive texlive-xetex texlive-latex-extra texlive-pstricks
RUN apt-get install -y lmodern fonts-thai-tlwg
RUN which xelatex

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000
CMD ["python", "app.py"]
