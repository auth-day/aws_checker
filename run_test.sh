#!/bin/bash
#

set -xe

function run_flake8 {
	apt install python-pip -y
   	pip install flake8
  	flake8 aws_checker/aws_checker.py

}

run_flake8
