

import random
import numpy as np

def prob(example_inputs, variations=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            all_results = []

            for example in example_inputs:
                example_results = []
                for _ in range(variations):
                    # Use generate_variations to create input variations
                    variation = generate_variations(example)
                    
                    # Run the test function with varied input
                    result = func(variation, **kwargs)
                    example_results.append(result)
                
                # Collect results for this example
                all_results.append({
                    "example": example,
                    "mean_result": sum(example_results) / len(example_results),
                    "results": example_results
                })
                
                print(f"Example '{example}' ran with {variations} variations.")
                print(f"Mean result for example: {all_results[-1]['mean_result']}")
                
            return all_results
        return wrapper
    return decorator


def generate_variations(example):
    print("hello world")