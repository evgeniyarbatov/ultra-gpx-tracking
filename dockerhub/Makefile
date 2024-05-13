build:
	terraform apply \
	-var 'image_name=gpx-postgis' \
	-var 'source_path=../postgis' \
	-auto-approve

	terraform apply \
	-var 'image_name=gpx-frontend' \
	-var 'source_path=../frontend' \
	-auto-approve

	terraform apply \
	-var 'image_name=gpx-backend' \
	-var 'source_path=../backend' \
	-auto-approve