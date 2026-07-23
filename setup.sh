#!/bin/bash

export OMPI_MC_opal_cuda_support="false"

export PATH=/home/cspark/Work/simulation_codes-working/warpx/install/bin:$PATH

if [ -z "$LD_LIBRARY_PATH" ]; then
    export LD_LIBRARY_PATH="/home/cspark/Work/simulation_codes-working/warpx/install/lib"
else
    export LD_LIBRARY_PATH="/home/cspark/Work/simulation_codes-working/warpx/install/lib:$LD_LIBRARY_PATH"
fi

export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH

conda activate warpx-dev

export WARPX_DATA_DIR=/home/cspark/Work/simulation_codes-working/warpx-data

