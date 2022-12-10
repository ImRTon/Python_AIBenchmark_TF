call conda create --name AIBenchmark_GPU python=3.9 -y
call conda activate AIBenchmark_GPU
call conda install -c conda-forge onednn -y
call conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
pip install -r requirements.txt