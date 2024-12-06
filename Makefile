validate:
	sam validate

login:
	aws sso login

invoke:
	sam build
	cp  ~/SCRIPTS/aws/aws-sam/cacert.pem .aws-sam/build/GetByEmail/certifi
	sam local invoke

debug:
	sam local invoke --debug
