# Steps to Correctly Set Up the Service Account:
- 
- 
    # Create a Service Account:
    - 
        - Go to the Google Cloud Console.
        - Select your project.
        - Navigate to "IAM & Admin" > "Service Accounts".
        - Click "Create Service Account".
        - Fill in the necessary details and click "Create".
        - Grant the service account appropriate roles, e.g., Viewer for read-only access.
        - Click "Continue" and then "Done".
        - Generate and Download the Service Account Key:

    # After creating the service account, find it in the list and click on it.
    -
        - Go to the "Keys" tab.
        - Click "Add Key" > "Create New Key".
        - Choose JSON as the key type and click "Create".
        - The JSON file will be downloaded automatically.
        - Place the JSON File in Your Django Project:

    - Save the downloaded JSON file in a secure location within your project directory.
    - Make sure this file is not publicly accessible.
