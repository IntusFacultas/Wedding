#!/bin/bash

pushd .

cd dist/js
find . -regex '.*/chunk.+\.js' -exec mv {} vendor.js \;
find . -regex '.*/app.+\.js' -exec mv {} app.js \;

cd ../css
find . -regex '.*/app.+\.css' -exec mv {} app.css \;

popd

rm -rf ../static/js
rm -rf ../static/css
rm -rf ../static/img

cp -r dist/img ../static/img
cp -r dist/js ../static/js
cp -r dist/css ../static/css