from ai_benchmark import AIBenchmark
import tensorflow as tf

print("==== AI Benchmark for CPU ====")
print("Tensorflow version:", tf.__version__)
benchmark = AIBenchmark(use_CPU=True, verbose_level=1)
results = benchmark.run(precision="normal")