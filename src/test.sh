cd __test__/

for file in `\find . -maxdepth 1 -type f -name "*.test.py"`; do
    python $file
done

cd ../