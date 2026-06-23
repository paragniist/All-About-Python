from empty_loop import heavy_work

def test_benchmark_heavy(benchmark):
    benchmark(heavy_work)