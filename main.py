#!/usr/bin/env python3
"""
Cerebras Code Explainer - Real-time code explanation using Qwen3 model
"""

import time
from utils.api_client import CerebrasClient

def display_banner():
    """Display a welcome banner"""
    print("\n" + "="*50)
    print("CEREBRAS CODE EXPLAINER".center(50))
    print(f"Powered by Qwen3".center(50))
    print("="*50 + "\n")

def get_user_code():
    """Collect multi-line code input from user"""
    print("Paste your code below (Press Ctrl+D when finished):\n")
    code = []
    try:
        while True:
            line = input()
            code.append(line)
    except EOFError:
        pass
    return '\n'.join(code)

def main():
    client = CerebrasClient()
    display_banner()
    
    while True:
        code = get_user_code()
        if not code.strip():
            print("\nNo code entered. Exiting...")
            break
            
        print("\nAnalyzing code...")
        start_time = time.time()
        
        try:
            response = client.generate_text(
                f"""Explain ONLY the following code in 3-5 bullet points. Do not continue writing after the explanation.
                
            Code:
            {code}

            Bullet points:
            1. """
            )
            
            if isinstance(response, dict) and 'error' in response:
                print(f"\nAPI Error: {response['error']}")
                continue
                
            if not isinstance(response, dict) or 'choices' not in response:
                print("\nError: Invalid API response format")
                continue
                
            explanation = response['choices'][0]['text'].split('\n\n')[0]
            if not explanation.strip().endswith('.'):
                explanation = explanation.split('The output will be:')[0].strip()
                if not explanation.endswith('.'):
                    explanation += '.'
            elapsed = time.time() - start_time
            
            print(f"\n=== Explanation === (Generated in {elapsed:.2f}s)")
            if response.get('model'):
                print(f"(Model: {response['model']})")
            print(explanation)
            
        except Exception as e:
            print(f"\nError during analysis:")
            print(f"- Check your internet connection")
            print(f"- Verify API key in .env")
            print(f"\nTechnical details: {str(e)}")
        
        if input("\nAnalyze another code snippet? (y/n): ").lower() != 'y':
            break
if __name__ == "__main__":
    main()
