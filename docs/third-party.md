## This for third party


To enable secure installation of third-party Python libraries in our Databricks environment on AWS GovCloud, we have two options. The first is to open outbound access to public PyPI, which is simple but poses security and compliance risks. The recommended approach is to build a private PyPI mirror using Bandersnatch within our VPC, ensuring full control over packages while maintaining compliance with GovCloud security standards. This setup allows safe and scalable access to approved Python libraries for data and analytics workloads.

## Best Practice in Regulated Environments:


✅ Use Bandersnatch to mirror only whitelisted packages

✅ Host your internal PyPI mirror inside GovCloud VPC (e.g., via S3 + CloudFront, or EC2 with Nginx)

✅ In Databricks, configure pip to point to this internal repo:

`
pip install --index-url https://<your-internal-pypi-mirror>/simple <package-name>
Or configure /databricks/python3/bin/pip.conf (via init script):
`

ini
`[global]
index-url = https://<your-internal-pypi-mirror>/simple
`
