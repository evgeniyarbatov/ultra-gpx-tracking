gencode:
	source ~/.venv/bin/activate && (\
		python3.12 -m grpc_tools.protoc \
		-I gpxtracker \
		--python_out=backend/src \
		--pyi_out=backend/src \
		--grpc_python_out=backend/src \
		gpxtracker/gpxtracker.proto \
	)

	npx grpc_tools_node_protoc \
	-I gpxtracker \
	--js_out=import_style=commonjs,binary:frontend/src \
	--grpc_out=frontend/src \
	--plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` \
	gpxtracker/gpxtracker.proto

