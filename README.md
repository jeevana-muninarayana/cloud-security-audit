# Cloud Security Audit Toolkit

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

Automated toolkit for continuous cloud configuration audits on AWS and GCP, with compliance benchmarks and IAM policy analysis.

## Organization-Relevant Value

Aligns directly with multiple organizations' need for scalable, programmatic review of infrastructure — complements AppSec tooling with automated detection of policy misconfigurations.

## Features
- IAM misconfiguration scanner
- CIS benchmark rule audit for AWS/GCP
- Slack/email integration for report alerts

## Stack
- Python, Boto3, GCP SDK
- Terraform Scanner
- CIS Benchmarks

## Setup

```bash
git clone https://github.com/jeevana-muninarayana/cloud-security-audit
cd cloud-security-audit
pip install -r requirements.txt
