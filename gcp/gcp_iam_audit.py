import subprocess

def list_gcp_roles():
    try:
        result = subprocess.run(['gcloud', 'iam', 'roles', 'list'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error listing GCP IAM roles:", e)

if __name__ == "__main__":
    list_gcp_roles()