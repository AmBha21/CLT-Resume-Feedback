import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase Admin SDK with the provided service account key
cred = credentials.Certificate("data/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def create_account_firebase(email, password, username):
    try:
        # Create user in Firebase Authentication
        user = auth.create_user(
            email=email,
            password=password,
            display_name=username  # Set the display name to the username
        )

        # Store additional user details in Firestore
        db = firestore.client()
        user_data = {
            "username": username,
            "email": email
        }
        user_ref = db.collection("users").document(user.uid)
        user_ref.set(user_data)

        print("Account created successfully.")
        return user.uid
    except Exception as e:
        print("Error creating account:", str(e))
        return None

def sign_in_firebase(email, password):
    try:
        # Sign in user with Firebase Authentication
        user = auth.get_user_by_email(email)
        auth.get_user(user.uid)
        print("Successfully signed in.")
        return user.uid
    except Exception as e:
        print("Error signing in:", str(e))
        return None