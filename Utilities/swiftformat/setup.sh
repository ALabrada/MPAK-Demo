#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" ; pwd -P)

SWIFTFORMAT_VERSION="0.48.1"
SWIFTFORMAT_DIR=$SCRIPT_DIR/.ignore/$SWIFTFORMAT_VERSION

if [ ! -d $SWIFTFORMAT_DIR ]; then
  git clone --branch $SWIFTFORMAT_VERSION https://github.com/nicklockwood/SwiftFormat $SWIFTFORMAT_DIR
fi

swift build --package-path $SWIFTFORMAT_DIR