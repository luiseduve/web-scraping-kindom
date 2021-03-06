import os, json, csv

# Array of original keys in the file
DB_KEY_FOLDER  = "db_key/"

FIREBASE_DB_KEY_EXT = ".json" 
FIREBASE_KEYS_LIST = ["type", "project_id", "private_key_id", "private_key", 
                "client_email", "client_id", "auth_uri", "token_uri", 
                "auth_provider_x509_cert_url", "client_x509_cert_url"]

FIREBASE_API_LIST = ["project_info","client","configuration_version"]

#####################
######### FUNCTIONS
#####################

def get_firebase_db_key(return_dict = False):
    """
    Returns the dict or the path of the private key used to connect to firebase app
    """
    dict_file = None
    for file in os.listdir(DB_KEY_FOLDER):
        # Open files that are Json
        if file.endswith(FIREBASE_DB_KEY_EXT):
            try:          
                with open(DB_KEY_FOLDER+file) as f:
                    dict_file = json.load(f)

                # If the dictionary is the same than the expected keys
                if (FIREBASE_KEYS_LIST == list(dict_file.keys())):
                    print("Dictionary for Firebase was found from:", DB_KEY_FOLDER+file)
                    if (return_dict):
                        return dict_file
                    else:
                        return DB_KEY_FOLDER+file
            except:
                continue

    print("Firebase database private key not found")
    return 1

def get_firebase_google_services(return_dict = False):
    """
    Returns the dict or the path of the private key used to connect to firebase API app
    """
    dict_file = None
    for file in os.listdir(DB_KEY_FOLDER):
        # Open files that are Json
        if file.endswith(FIREBASE_DB_KEY_EXT):
            try:          
                with open(DB_KEY_FOLDER+file) as f:
                    dict_file = json.load(f)

                # If the dictionary is the same than the expected keys
                if (FIREBASE_API_LIST == list(dict_file.keys())):
                    print("Firebase google-services found from:", DB_KEY_FOLDER+file)
                    if (return_dict):
                        return dict_file
                    else:
                        return DB_KEY_FOLDER+file
            except:
                continue

    print("Firebase google-services for API not found")
    return 1