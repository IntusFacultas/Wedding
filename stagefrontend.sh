#!/bin/bash

pushd .

cd dist/js
find . -regex '.*/chunk.+\.js' -exec mv {} vendor.js \;
find . -regex '.*/app.+\.js' -exec mv {} app.js \;

cd ../css
find . -regex '.*/app.+\.css' -exec mv {} app.css \;

popd

rm -rf api/static/js
rm -rf api/static/css
rm -rf api/static/img

cp -r dist/img api/static/img
cp -r dist/js api/static/js
cp -r dist/css api/static/css