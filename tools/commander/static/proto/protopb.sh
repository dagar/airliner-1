#!/usr/bin/env bash
protoc -I=. --python_out=. *.proto
