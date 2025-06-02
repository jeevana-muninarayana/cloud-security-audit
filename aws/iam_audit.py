import boto3

def list_roles():
    client = boto3.client('iam')
    roles = client.list_roles()
    for role in roles['Roles']:
        print(f"Role: {role['RoleName']} - Created on: {role['CreateDate']}")

if __name__ == "__main__":
    list_roles()