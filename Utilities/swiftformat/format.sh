#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" ; pwd -P)

SWIFTFORMAT_VERSION="0.48.1"
SWIFTFORMAT_DIR=$SCRIPT_DIR/.ignore/$SWIFTFORMAT_VERSION

$SWIFTFORMAT_DIR/CommandLineTool/swiftformat --config $SCRIPT_DIR/swiftformat $SCRIPT_DIR/../../demo $SCRIPT_DIR/../../Modules --swiftversion 5