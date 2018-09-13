FROM python:2

ARG build_date
ARG commit_hash
ARG commit_owner

LABEL build_date="${build_date}"
LABEL commit_hash="${commit_hash}"
LABEL commit_owner="${commit_owner}"

ADD aws_checker/aws_checker.py /
ADD aws_checker/aws_config.yml /

COPY requirements.txt /
RUN pip install -r /requirements.txt

ENTRYPOINT [ "python", "/aws_checker.py" ]
