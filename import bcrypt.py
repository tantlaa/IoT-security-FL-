import bcrypt
password = b"secret passwordd 0333"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
b'8bcaa90d981a4c786ecf5ac407adc40de2b6ffdc4fe4a00788e6653554ea6cdb'
b'ba86dcd6794b2b207cec25b37e04b6be00b70ee26fd4eda1c4'