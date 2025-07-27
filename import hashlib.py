import hashlib

# Simulated values (as bytes or strings)
A_i_IoT = "PACKETS_FROM_DEVICE_1"
A_i_fusion = "PACKETS_FROM_DEVICE_1"  # Change this to simulate mismatch
N_i = "NONCE_12345"
K_vi = "PRIVATE_KEY_ABC123"

# Function to generate hash (H(A, N, K))
def generate_hash(data, nonce, key):
    combined = f"{data}|{nonce}|{key}".encode('utf-8')
    return hashlib.sha256(combined).hexdigest()

# IoT device computes its feedback
fv = generate_hash(A_i_IoT, N_i, K_vi)

# Fusion center computes its expected feedback
fs = generate_hash(A_i_fusion, N_i, K_vi)

# Comparison
print("ƒᵥ (From IoT):", fv)
print("ƒₛ (Expected):", fs)

if fv == fs:
    print("✅ Device trusted – No anomaly detected.")
else:
    print("⚠️ Anomaly detected – Data mismatch!")
