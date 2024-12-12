import pandas as pd
import numpy as np
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the output directory exists
output_dir = 'backend/data/'
os.makedirs(output_dir, exist_ok=True)
logging.info(f"Output directory: {output_dir} created or already exists.")

# Function to generate a new Virality dataset with all cases included
def generate_related_virality_data(num_samples=5000):
    logging.debug("Generating Virality dataset...")
    data = {
        'likes': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'comments': np.random.randint(0, 5000, num_samples),
        'weak_ties': np.random.rand(num_samples) * 10
    }
    df = pd.DataFrame(data)
    df['virality_label'] = (
        ((df['likes'] > 7000) & (df['shares'] > 3000)) |
        ((df['likes'] > 7000) & (df['shares'] < 3000)) |
        ((df['likes'] > 7000) & (df['shares'].between(2000, 4000))) |
        ((df['shares'] > 4000) & (df['comments'] > 2000)) |
        ((df['likes'] > 5000) & (df['weak_ties'] > 6)) |
        ((df['shares'] > 4000) & (df['weak_ties'] > 5))
    ).astype(int)
    logging.debug("Virality dataset generation complete.")
    return df

# Function to generate a new Influencer dataset with all cases included
def generate_related_influencer_data(num_samples=5000):
    logging.debug("Generating Influencer dataset...")
    data = {
        'followers': np.random.randint(1000, 1000000, num_samples),
        'posts': np.random.randint(10, 1000, num_samples),
        'likes': np.random.randint(0, 100000, num_samples),
        'comments': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'engagement_rate': np.random.rand(num_samples) * 10
    }
    df = pd.DataFrame(data)
    df['is_influencer'] = (
        ((df['followers'] > 500000) & (df['engagement_rate'] > 5)) |
        ((df['followers'] > 100000) & (df['posts'] > 300) & (df['likes'] > 50000)) |
        ((df['engagement_rate'] > 8) & (df['comments'] > 5000)) |
        ((df['followers'] < 50000) & (df['engagement_rate'] > 8))
    ).astype(int)
    logging.debug("Influencer dataset generation complete.")
    return df

# Function to generate a new Diffusion (Misinformation) dataset with all cases included
def generate_related_diffusion_data(num_samples=5000):
    logging.debug("Generating Diffusion dataset...")
    data = {
        'likes': np.random.randint(0, 10000, num_samples),
        'shares': np.random.randint(0, 5000, num_samples),
        'comments': np.random.randint(0, 5000, num_samples),
        'engagement_rate': np.random.rand(num_samples) * 10
    }
    df = pd.DataFrame(data)
    df['is_misinformation'] = (
        ((df['likes'] > 8000) & (df['shares'] > 3000) & (df['comments'] > 2000)) |
        ((df['engagement_rate'] > 8) & (df['shares'] > 4000)) |
        ((df['likes'] > 6000) & (df['comments'] > 4000) & (df['engagement_rate'] > 7)) |
        ((df['shares'] > 2000) & (df['engagement_rate'] > 9))
    ).astype(int)
    logging.debug("Diffusion dataset generation complete.")
    return df

# Main function to generate and save datasets
def main():
    try:
        logging.info("Starting dataset generation process...")
        virality_data = generate_related_virality_data()
        influencer_data = generate_related_influencer_data()
        diffusion_data = generate_related_diffusion_data()

        # Save the datasets
        virality_data.to_csv(os.path.join(output_dir, 'virality_data.csv'), index=False)
        influencer_data.to_csv(os.path.join(output_dir, 'influencer_data.csv'), index=False)
        diffusion_data.to_csv(os.path.join(output_dir, 'diffusion_data.csv'), index=False)

        logging.info("Datasets successfully generated and saved:")
        logging.info("- virality_data.csv")
        logging.info("- influencer_data.csv")
        logging.info("- diffusion_data.csv")
    except Exception as e:
        logging.error(f"An error occurred during dataset generation: {e}")

# Run the script
if __name__ == '__main__':
    main()
