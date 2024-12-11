import pandas as pd
import numpy as np
import os

# Ensure the output directory exists
output_dir = 'backend/data/'
os.makedirs(output_dir, exist_ok=True)

# Set a seed for reproducibility
np.random.seed(42)

# 1. Generate Virality Prediction Dataset
def generate_virality_data(num_samples=5000):
    data = {
        'content_id': np.arange(1, num_samples + 1),
        'likes': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'comments': np.random.randint(0, 5000, num_samples),
        'weak_ties': np.random.rand(num_samples) * 10,
        'is_viral': np.random.choice([0, 1], num_samples, p=[0.7, 0.3])
    }
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(output_dir, 'virality_data.csv'), index=False)
    print("Virality dataset generated and saved to virality_data.csv")

# 2. Generate Influencer Identification Dataset
def generate_influencer_data(num_samples=5000):
    data = {
        'user_id': np.arange(1, num_samples + 1),
        'followers': np.random.randint(1000, 1000000, num_samples),
        'posts': np.random.randint(10, 1000, num_samples),
        'likes': np.random.randint(0, 100000, num_samples),
        'comments': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'engagement_rate': np.random.rand(num_samples) * 10,
        'is_influencer': np.random.choice([0, 1], num_samples, p=[0.6, 0.4])
    }
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(output_dir, 'influencer_data.csv'), index=False)
    print("Influencer dataset generated and saved to influencer_data.csv")

# 3. Generate Diffusion Prediction Dataset (Misinformation Detection)
def generate_diffusion_data(num_samples=5000):
    data = {
        'content_id': np.arange(1, num_samples + 1),
        'likes': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'comments': np.random.randint(0, 5000, num_samples),
        'engagement_rate': np.random.rand(num_samples) * 10,
        'narrative_type': np.random.choice([0, 1], num_samples, p=[0.8, 0.2])  # 20% misinformation
    }
    df = pd.DataFrame(data)
    print("Sample diffusion_data preview:\n", df.head())  # Verify contents before saving
    df.to_csv(os.path.join(output_dir, 'diffusion_data.csv'), index=False)
    print("Diffusion dataset generated and saved to diffusion_data.csv")

# Run all generators
def main():
    generate_virality_data()
    generate_influencer_data()
    generate_diffusion_data()

if __name__ == '__main__':
    main()
