run:
	docker run -it -d --env-file .env --restart=unless-stopped --name bot_doc riotwwks/tbpgs
stop:
	docker stop bot_doc
attach:
	docker attach bot_doc
dell:
	docker rm bot_doc