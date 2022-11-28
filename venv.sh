#!/bin/bash
script_dir=`dirname $0`
cd $script_dir
/bin/bash -c ". ./venv/bin/activate; exec /bin/bash -i"
