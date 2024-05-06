gencode:
	source ~/.venv/bin/activate && (\
		python3.12 -m grpc_tools.protoc \
		-I gpxtracker \
		--python_out=backend/src \
		--pyi_out=backend/src \
		--grpc_python_out=backend/src \
		gpxtracker/gpxtracker.proto \
	)

	cp \
	gpxtracker/gpxtracker.proto \
	frontend/src/gpxtracker

