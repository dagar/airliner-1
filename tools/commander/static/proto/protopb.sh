#!/usr/bin/env bash
protoc -I=. --python_out=. *.proto
protoc -I=. --js_out=import_style=commonjs,binary:build/gen  *.proto