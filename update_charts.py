import os
import shutil

services = [
    {
        'name': 's3',
        'version': 'v0.1.4'
    },
    {
        'name': 'sfn',
        'version': 'v0.1.0'
    },
    {
        'name': 'elasticache',
        'version': 'v0.0.20'
    },
    {
        'name': 'sns',
        'version': 'v0.0.2'
    },
    {
        'name': 'ecr',
        'version': 'v0.1.5'
    },
    {
        'name': 'dynamodb',
        'version': 'v0.1.4'
    },
    {
        'name': 'apigatewayv2',
        'version': 'v0.1.3'
    },
    {
        'name': 'mq',
        'version': 'v0.0.20'
    },
    {
        'name': 'rds',
        'version': 'v0.1.0'
    }
]

os.environ['HELM_EXPERIMENTAL_OCI'] = '1'

chart_export_path = './charts'
chart_repo = 'public.ecr.aws/aws-controllers-k8s'

shutil.rmtree(chart_export_path)
# os.system('mkdir -p $CHART_EXPORT_PATH')

for service in services:
    chart_ref = 'oci://%s/%s-chart --version %s --destination %s --untar true' % (chart_repo, service['name'], service['version'], chart_export_path)
    print(chart_ref)
    os.system('helm pull %s' % chart_ref)
    if service['name'] == 'sns':
        os.system('cp -R ./charts/ack-sns-controller/* ./charts/sns-chart')
        os.system('rm -rf ./charts/ack-sns-controller')

