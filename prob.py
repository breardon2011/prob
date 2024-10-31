

import random
import numpy as np
from prob_types import ExampleInput

def prob(example_inputs: list[ExampleInput], generate=False, variations=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            all_results = []

            for example_input in example_inputs:
                example_results = []
                for _ in range(variations):
                    # Conditionally generate variations or use the example input
                    variation = generate_variations(example_input.example) if generate else example_input.example
                    
                    # Run the test function with the input (either generated or original)
                    result = func(variation, **kwargs)
                    example_results.append(result)
                
                # Collect results for this example
                all_results.append({
                    "example": example_input.example,
                    "expected": example_input.expected,
                    "results": example_results
                })
                
                print(f"Example '{example_input.example}' ran with {variations} variations.")
                print(f"Expected result: {example_input.expected}")
                print(f"Mean result for example: {all_results[-1]['mean_result']}")
                
            return all_results
        return wrapper
    return decorator


def generate_variations(example):
    print("hello world")