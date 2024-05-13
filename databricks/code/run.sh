filetype=".py .sql"

for ftype in $filetype
do
    echo "Running $ftype files"
    for file in $(find . -name "*$ftype")
    do
        echo "Running $file"
        databricsk workspace mkdirs $ws_root
        if [ $ftype == ".py" ]
        then
            databricks workspace import -l PYTHON -f $file $ws_root
        elif [ $ftype == ".sql" ]
        then
            databricks workspace import -l SQL -f $file $ws_root
            # sqlplus -s $file
        fi
    done
done