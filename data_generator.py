import numpy as np
import pandas as pd
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_rssi_data(n_samples=5000):
    """Generate synthetic RSSI data with normal and anomalous behaviors."""
    data = []
    labels = []
    
    # Normal behavior: RSSI typically between -90 and -30 dBm
    normal_rssi = np.random.normal(loc=-60, scale=10, size=int(n_samples * 0.6))
    
    # Anomalous behaviors
    spoofing_rssi = np.random.normal(loc=-50, scale=5, size=int(n_samples * 0.1))  # Tighter range for spoofing
    jamming_rssi = np.random.uniform(low=-100, high=-80, size=int(n_samples * 0.1))  # Low signal due to jamming
    replay_rssi = np.random.normal(loc=-60, scale=2, size=int(n_samples * 0.1))  # Very stable signal
    eavesdropping_rssi = np.random.normal(loc=-70, scale=15, size=int(n_samples * 0.1))  # Slightly erratic
    
    # Combine data
    rssi_values = np.concatenate([normal_rssi, spoofing_rssi, jamming_rssi, replay_rssi, eavesdropping_rssi])
    labels = [0] * len(normal_rssi) + [1] * (len(rssi_values) - len(normal_rssi))
    
    return pd.DataFrame({
        'RSSI': rssi_values,
        'Label': labels
    })

def generate_csi_data(n_samples=5000):
    """Generate synthetic CSI data with multiple subcarriers."""
    data = []
    labels = []
    
    # CSI: Simulate 30 subcarriers (complex values simplified to magnitude)
    normal_csi = np.random.normal(loc=0, scale=1, size=(int(n_samples * 0.6), 30))
    spoofing_csi = np.random.normal(loc=0, scale=0.5, size=(int(n_samples * 0.1), 30))  # Reduced variance
    jamming_csi = np.random.uniform(low=-2, high=2, size=(int(n_samples * 0.1), 30))  # Noise-like
    replay_csi = np.repeat(np.random.normal(loc=0, scale=1, size=(1, 30)), int(n_samples * 0.1), axis=0)  # Repeated pattern
    eavesdropping_csi = np.random.normal(loc=0, scale=1.5, size=(int(n_samples * 0.1), 30))  # Higher variance
    
    # Combine data
    csi_values = np.vstack([normal_csi, spoofing_csi, jamming_csi, replay_csi, eavesdropping_csi])
    labels = [0] * len(normal_csi) + [1] * (len(csi_values) - len(normal_csi))
    
    return pd.DataFrame(csi_values, columns=[f'Subcarrier_{i}' for i in range(30)]), pd.Series(labels)

def generate_tof_data(n_samples=5000):
    """Generate synthetic ToF data."""
    data = []
    labels = []
    
    # Normal behavior: ToF in nanoseconds
    normal_tof = np.random.normal(loc=50, scale=5, size=int(n_samples * 0.6))
    spoofing_tof = np.random.normal(loc=45, scale=2, size=int(n_samples * 0.1))  # Slightly off
    jamming_tof = np.random.uniform(low=0, high=20, size=int(n_samples * 0.1))  # Unreliable ToF
    replay_tof = np.random.normal(loc=50, scale=1, size=int(n_samples * 0.1))  # Very consistent
    eavesdropping_tof = np.random.normal(loc=60, scale=7, size=int(n_samples * 0.1))  # Delayed
    
    # Combine data
    tof_values = np.concatenate([normal_tof, spoofing_tof, jamming_tof, replay_tof, eavesdropping_tof])
    labels = [0] * len(normal_tof) + [1] * (len(tof_values) - len(normal_tof))
    
    return pd.DataFrame({
        'ToF': tof_values,
        'Label': labels
    })

def save_datasets():
    """Save generated datasets to CSV files."""
    os.makedirs('data', exist_ok=True)
    
    rssi_df = generate_rssi_data()
    rssi_df.to_csv('data/rssi_data.csv', index=False)
    
    csi_df, csi_labels = generate_csi_data()
    csi_df['Label'] = csi_labels
    csi_df.to_csv('data/csi_data.csv', index=False)
    
    tof_df = generate_tof_data()
    tof_df.to_csv('data/tof_data.csv', index=False)

if __name__ == "__main__":
    save_datasets()
    print("Synthetic datasets generated and saved in 'data' directory.")