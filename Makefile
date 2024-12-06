validate:
	sam validate

login:
	aws sso login

build:
	sam build

deploy: build
	sam deploy

invoke: build
	cp  ~/SCRIPTS/aws/aws-sam/cacert.pem .aws-sam/build/GetByEmail/certifi
	sam local invoke --debug

test:
	aws lambda invoke --function-name okta-api-access-GetByEmail-7XFMQPSOJkiB test.out
	cat test.out

all: deploy test

