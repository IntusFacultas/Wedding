#!/bin/bash

pushd .

cd dist/js
find . -regex '.*/chunk.+\.js' -exec mv {} vendor.js \;
find . -regex '.*/app.+\.js' -exec mv {} app.js \;
gzip -9 vendor.js
gzip -9 app.js

cd ../css
find . -regex '.*/chunk.+\.css' -exec mv {} vendor.css \;
find . -regex '.*/app.+\.css' -exec mv {} app.css \;
gzip -9 vendor.css
gzip -9 app.css

popd

rm -rf ../static/js
rm -rf ../static/css
rm -rf ../static/img

cp -r dist/img ../static/img
cp -r dist/js ../static/js
cp -r dist/css ../static/css