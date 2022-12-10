call conda create --name AIBenchmark python=3.9 -y
call conda activate AIBenchmark
call conda install -c conda-forge onednn -y
pip install -r requirements.txt