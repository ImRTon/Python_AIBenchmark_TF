from ai_benchmark import AIBenchmark
import tensorflow as tf

print("==== AI Benchmark for GPU ====")
print("Tensorflow version:", tf.__version__)
benchmark = AIBenchmark(use_CPU=False, verbose_level=1)
results = benchmark.run(precision="normal")